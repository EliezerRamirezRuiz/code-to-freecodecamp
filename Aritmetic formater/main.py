import logging


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def arithmetic_arranger(*args, state:bool):
  string_operator = ["+", "-"]
  
  if len(args) < 6:
    
    for i in args:
      objects = i.split(" ")
      
      if objects[1] == string_operator[0]:
        
        if int(objects[0]) and int(objects[2]) <= 9999:
          result = int(objects[0]) + int(objects[2])
          logging.info(f""" {objects[0]}\n{objects[1]}{objects[2]}\n---\n{result}
          \n\n\n\n""")
              
      elif objects[1] == string_operator[1]:
        
        if int(objects[0]) and int(objects[2]) <= 9999 :
          result = int(objects[0]) - int(objects[2])
          logging.info(f""" {objects[0]}\n{objects[1]}{objects[2]}\n---\n{result}
          \n\n\n\n""")
          
        else:
          logging.error("Error: Numbers cannot be more than four digits")
      
      else:
          logging.error('Operator must be (+) or (-) .- \n\n\n')
  else:
    logging.error("Error: Too many problems. \n\n\n")




arithmetic_arranger(
  "1 + 3",
  "5 + 2",
  "3247 - 5555",
  "7 - 2",
  "5 + 2",
  state=True
)
