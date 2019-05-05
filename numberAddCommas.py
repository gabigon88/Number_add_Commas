import re

def is_number(num):
  pattern = re.compile(r'^[-+]?[0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
  result = pattern.match(num)
  if result:
    return True
  else:
    return False

def addCommas(num):
  number = str(num).strip() #去頭尾空白
  resultList = list("")

  if (not is_number(number)):
    print("Error Input number '%s'" %num)
    return

  else:
    if ( (number[0] == '-') | (number[0] == '+') ):
      resultList.append(number[0])
      number = number[1:] #刪除開頭正負號

    if (number.find('.') >= 0):
      prefix, postfix = number.split('.')
    else:
      prefix = number
      postfix = ""
    
    if (len(prefix) <= 3):
      resultList.append(prefix)
      
    else:
      switch = len(prefix) % 3

      if (switch == 1):
        resultList.append(prefix[0])
        prefix = prefix[1:]
      elif (switch == 2):
        resultList.append(prefix[0:2])
        prefix = prefix[2:]

      while (len(prefix) > 0):
        resultList.append(',')
        resultList.append(prefix[0:3])
        prefix = prefix[3:]
        
    if (len(postfix) > 0):
      resultList.append('.')
      resultList.append(postfix)

    return "".join(resultList)