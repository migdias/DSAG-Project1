class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    stack = [] # Using a stack to recursively go to child groups in search of user

    # First check main group if the user is there
    for u in group.get_users():
        if u == user:
            return True
        
    # If not checks subgroups and appends to stack
    if len(group.get_groups()) > 0:
        for g in group.get_groups():
            stack.append(g)

    while True: # In a infinite loop
        # the break point is when there are no values in the stack
        if len(stack) == 0:
            return False
        
        # if there are, pop a group and check for users and subgroups
        new_group = stack.pop()

        # if the user is found then return
        for u in new_group.get_users():
            if u == user:
                return True
        
        if len(new_group.get_groups()) > 0:
            for g in new_group.get_groups():
                stack.append(g)


if __name__ == '__main__':
    parent = Group("parent")
    parent2 = Group("parent2")

    child = Group("child")
    sub_child = Group("subchild")
    sub_child_2 = Group("subchild2")
    sub_sub_child = Group("subsubchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    # add groups
    child.add_group(sub_child)
    child.add_group(sub_child_2)
    parent.add_group(child)
    sub_child_2.add_group(sub_sub_child)

    [parent2.add_user(f'user{x}') for x in range(200,205)]
    [parent.add_user(f'user{x}') for x in range(5)]
    [child.add_user(f'user{x}') for x in range(5, 10)]
    [sub_child.add_user(f'user{x}') for x in range(50, 60)]
    [sub_child_2.add_user(f'user{x}') for x in range(28, 38)]
    [sub_sub_child.add_user(f'user{x}') for x in range(100, 106)]

    ## Add your own test cases: include at least three test cases
    ## and two of them must include edge cases, such as null, empty or very large values

    ## Test Case 1 -- Completely separate groups
    assert is_user_in_group('user201', parent2), 'user201 should belong dirently to parent2'
    assert not is_user_in_group('user201', parent), 'user201 should not belong to parent1 or any of its subfolders'

    # Add the same user to the other parent and it should be findable
    sub_sub_child.add_user('user201')
    assert is_user_in_group('user201', parent), 'user201 now belong to parent, since it belongs to one of its subgroups'

    ## Test Case 2 -- user directly belonging to a subsubchild
    assert is_user_in_group('user30', sub_child_2), 'user201 should belong to subchild2'
 

    ## Test Case 3 -- user belongs to parent, child, and subchild but not subsubchild
    assert is_user_in_group('user55', parent), 'user55 should belong to child'
    assert is_user_in_group('user55', child), 'user55 should belong to child'
    assert is_user_in_group('user55', sub_child), 'user55 should belong to subchild'
    assert not is_user_in_group('user55', sub_child_2), 'user55 should NOT belong to subchild2'

    ## Test Case 3 -- Typo should return False
    assert not is_user_in_group('user_55', parent), 'Should return False has its a typo'