from utils import get_puzzle_input

id_ranges = get_puzzle_input(2).strip('\n').split(',')

# Part 1
def get_ids(id_range):
    first_id, last_id = id_range.split('-') 
    return [id for id in range(int(first_id), int(last_id) + 1)]

def get_invalid_ids(ids):
    return [id for id in ids if is_id_invalid(id)]

def is_id_invalid(id):
    id = str(id)
    id_length = len(id)
    
    if (id_length % 2 != 0):
        return False
    
    return id[:id_length // 2] == id[id_length // 2:]

def get_invalid_id_sum():
    invalid_id_sum = 0

    for id_range in id_ranges:
        invalid_ids = get_invalid_ids(get_ids(id_range))
        invalid_id_sum += sum(invalid_ids)

    return invalid_id_sum

print(get_invalid_id_sum())

# Part 2

def get_id_slices(id, slice_size):
    return [int(id[slice_start_index:slice_start_index + slice_size]) for slice_start_index in range(0, len(id), slice_size)]

def is_id_invalid2(id):
    id = str(id)
    id_length = len(id)

    if (id_length == 1):
        return False
    
    if (len(set(get_id_slices(id, 1))) == 1):
        return True

    start_index = 2

    if (id_length % 2 != 0):
        start_index = 3

    for slice_size in range(start_index, id_length // 2 + 1, 1):
        if (len(set(get_id_slices(id, slice_size))) == 1):
            return True
            
    return False

def get_invalid_ids2(ids):
    return [id for id in ids if is_id_invalid2(id)]

def get_invalid_id_sum2():
    invalid_id_sum = 0

    for id_range in id_ranges:
        invalid_ids = get_invalid_ids2(get_ids(id_range))
        invalid_id_sum += sum(invalid_ids)

    return invalid_id_sum

print(get_invalid_id_sum2())