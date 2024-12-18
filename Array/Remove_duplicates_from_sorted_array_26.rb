def method(arr)
  result = []
  # add element in arr into result
  arr.each do |element|
    # if element isn't  in result  add in it
    result << element unless result.include?(element)
  end
  result
end

arr = [1,1,2,2,3,4]
# output [1,2,3,4]

# 用双指针法
def method(arr)
  array_new = []
  arr.each_index do |i|
    # add arr[i] to array_new unless arr[i] = arr[i-1]
    array_new << arr[i] unless arr[i] == arr[i - 1]
  end
  array_new
end
