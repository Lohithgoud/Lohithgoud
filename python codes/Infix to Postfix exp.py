# Convert Infix expression to Postfix expression

def prec(c):
  if c == "^":
    return 3
  elif(c == "/" or c== "*"):
    return 2
  elif( c== "+" or c == "-"):
    return 1
  else:
    return -1

def assco(c):
  if(c == "^"):
    return "R"
  else:
    return "L"

def postfix(exp):
  res = []
  stack = []
  
  for i in range(len(exp)):
    c = exp[i]
    
    if("a" <= c <= "z") or ("A" <= c <= "Z" ) or ( "0" <= c <= "9" ):
      res.append(c)
      
    elif( c == "("):
      stack.append(c)
    
    elif(c == ")"):
      while stack and stack != "(" :
        res.append(stack.pop())
        stack.pop()
      
    else:
      while stack and (prec(exp[i]) < prec(stack[-1]) or
                            (prec(exp[i]) == prec(stack[-1]) and assco(exp[i]) == 'L')):
      # while stack and (prec(exp[i])< prec(stack[-1])) or ((prec(exp[i])== prec(stack[-1])) and (assco(exp[i])== 'L')):
        res.append(stack.pop())
        
      stack.append(exp[i])
      
  while stack:
    res.append(stack.pop())
  
  print("".join(res))
      
      
      
ex = "a+b*(c^d-e)^(f+g*h)-i"
postfix(ex)    
      
      
      # abcd^e-fgh*+^*+i-
      