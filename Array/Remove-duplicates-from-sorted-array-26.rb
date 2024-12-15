def method(arr)
  result = []
 # add element in arr into result
  arr.each do |element|
    # if element isn't  in result  add in it
    result << element if !result.include?(element)
  end
  result
end

arr = [1,1,2,2,3,4]
# output [1,2,3,4]
