# frozen_string_literal: true

def reverse_string(str)
  i = 0
  j = str.length - 1
    while i < j
      str[i], str[j] = str[j], str[i]
      i += 1
      j -= 1
    end
  str
end

# str = %w[h e l l o]
# output = %w[o,l,l,e,h]
