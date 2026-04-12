def solution(phone_book): 

    hash_map = {} 
    for nums in phone_book: 
        hash_map[nums] = 1 
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
            if arr in hash_map and arr != nums:       
                return False 
                
    return True

if __name__ == "__main__":
    phone_book = solution(["119", "97674223", "1195524421"])
    print(phone_book)