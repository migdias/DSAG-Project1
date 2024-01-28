from collections import deque
import os



def find_files(suffix: str, path: str):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    path_stack = deque()
    path_list = []

    def _find_files(suffix: str, path: str, path_stack, path_list):
        #print(path)
        #print(f'Stack: {path_stack}')

        # if its a directory, add all to stack
        if os.path.isdir(path):
            for o in os.listdir(path):
                path_stack.append(os.path.join(path, o))
                #print(path_stack)

        # if its a file check if its with the suffix and append
        elif os.path.isfile(path):
            if path.endswith(suffix):
                path_list.append(path)

        # If the stack if empty, its done recursing
        if not path_stack:
            return path_list
        
        # Recall function with a new popped path
        new_path = path_stack.pop()
        _find_files(suffix=suffix, path=new_path, path_stack=path_stack, path_list=path_list)

    _find_files(suffix, path, path_stack, path_list)

    if len(path_list) == 0:
        return None
    
    return path_list

if __name__ == '__main__':
    path = 'resources/testdir'

    # find the ones with .c
    list_files = find_files(suffix = '.c', path = path)
    assert set(list_files) == {'resources/testdir/subdir1/a.c', 'resources/testdir/subdir3/subsubdir1/b.c', 'resources/testdir/subdir5/a.c', 'resources/testdir/t1.c'}, 'Not passed'

    # finding .py should return none
    list_files = find_files(suffix = '.py', path = path)
    assert list_files is None, 'list files is not none'

    # finding .gitkeep shoudl return only two 
    list_files = find_files(suffix = '.gitkeep', path = path)
    assert len(list_files) == 2, 'length not right'
    assert set(list_files) == {'resources/testdir/subdir4/.gitkeep', 'resources/testdir/subdir2/.gitkeep'}, 'result is wrong'

    # Searching a non-existant path should return None
    list_files = find_files(suffix = '.gitkeep', path = 'resources/test')
    assert list_files is None, 'list is not none'
