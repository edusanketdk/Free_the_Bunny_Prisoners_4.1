# used for itertools.combination(x,y) function.
# returns, in lexographically least order,
# every subset of [0,x-1] that contains y elements
import itertools

def answer(num_buns, num_required):
    a = []
    # conditionals aren't necessary, but will
    # make program faster and more memory
    # efficient in those cases

    # 1 key required, each bunny has one key
    if num_required==1:
        for i in range(num_buns):
            a.append([0])
        return a
    # num_buns keys required, each bunny has a unique key    
    elif num_buns==num_required:
        for i in range(num_buns):
            a.append([i])
        return a
    #every other combination of bunnies and keys    
    else:
        # populate first array dimension for each bunny
        for i in range(num_buns):
            a.append([])
        # no keys required, each bunny has no key
        if num_required==0:
            return a
        # total number of elements
		total=len(list(itertools.combinations(range(num_buns),num_required)))*num_required
        # how many bunnies have each key
        num_keys=num_buns-num_required+1
        # first dimension is each key used
        # second dimension is which bunnies get that key
        key_combs=list(itertools.combinations(range(num_buns),num_keys))

        # i iterates through each key used
        for i in range(total//num_keys):
            # j iterates through every bunny which gets that key
            for j in key_combs[i]:
                # give the current key (i) to bunny j
                a[j].append(i)
    return a
