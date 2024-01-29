# Problem 4 - Active Directory

For this problem I decided to use a Stack Structure along with a infinite loop.

Basically the same way as the find_files, from a previous problem. It takes a group, checks if the user is there directly. If its node, adds all subgroups to stack, and checks a subgroup one at a time until it finds the user. If it traverses all groups and users and it does not find it, then it returns that the user does not belong to the group.

The overall complexity is O(N + M), where N is the total number of groups in the hierarchy and M is the total number of users across all groups. The space complexity is O(n), where N is the total number of groups in the hierarchy since we use a stack to store subgroups during traversal.