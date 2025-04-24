from typing import List
import argparse

def binary_search(arr: List[int], target:int) -> int:
   left, right = 0, len(arr) -1
   while (left < right):
       mid = (left+right ) // 2
       if (arr[mid] < target):
          left = mid + 1
       elif (arr[mid] > target):
          right = mid - 1
       else:
          return mid
   
   return -1
   


if __name__ =='__main__':
   
   # prepare the input arguments
   parser = argparse.ArgumentParser(description='Binary Search CLI')
   parser.add_argument('--array', type=str, required=True, help='Comma-separated sorted array (e.g., 1,2,3,4,5)')
   parser.add_argument('--target', type=str, required=True, help='Target value to search')

   args = parser.parse_args()

   input_array = args.array.split(',')

   # convert input type
   def convert_type(x: str):
      for conv in (int, float):
          try:
              return conv(x)  
          except ValueError:
              continue
      return x
   
   input_array = list(map(convert_type,input_array))
   target = convert_type(args.target)

      

#    target_array = [0,1,2,3,4,5]
#    target_int = 4
   result = binary_search(input_array, target)
   if result > 0:
     print(f"Target {target} found at index: {result}")
   else:
     print(f"Not found!")