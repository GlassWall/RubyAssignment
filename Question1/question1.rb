def checkBalance?(exp)  
	stack = []
	for ch in exp.chars
		case ch
		when '('
		  stack << ')'
		when '{'
		  stack << '}'
		when '['
		  stack << ']'
		else
		  if stack.empty? || (stack.pop != ch)
		  	return false
		  end
		end 
	end
return stack.empty?
end 
puts(checkBalance?("()[]{}"))
puts(checkBalance?("([{}])"))
puts(checkBalance?("([]{})"))
puts(checkBalance?("([)]"))
puts(checkBalance?("([]"))
puts(checkBalance?("[])"))
puts(checkBalance?("([})"))