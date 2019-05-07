import re

#判斷是否為數字
def is_number(num):
  #表示式意思: 判斷小數|判斷整數
  pattern = re.compile(r'^[-+]?\d+\.\d+|[-+]?\d+$') 
  result = pattern.match(num)
  if result:
    return True
  else:
    return False

#為輸入的數字加上逗號
def addCommas(num):
  number = str(num).strip() #去頭尾空白
  resultList = list("")

  if (not is_number(number)):
    print("Error Input number '%s'" %num)
    return

  else:
    #處理開頭正負號
    if ( (number[0] == '-') | (number[0] == '+') ):
      resultList.append(number[0])
      number = number[1:]

    #依小數點將輸入分為前半與後半
    if (number.find('.') >= 0):
      prefix, postfix = number.split('.')
    else:
      prefix = number
      postfix = ""
    
    #如果小於3位數，不需加逗號
    if (len(prefix) <= 3):
      resultList.append(prefix)
    
    else:
      #每3位數當一組時，將會多出的位數(0~2個)做處理
      switch = len(prefix) % 3
      if (switch == 1):
        resultList.append(prefix[0])
        prefix = prefix[1:]
      elif (switch == 2):
        resultList.append(prefix[0:2])
        prefix = prefix[2:]

      #每3位數當一組做處理
      while (len(prefix) > 0):
        resultList.append(',')
        resultList.append(prefix[0:3])
        prefix = prefix[3:]

    #小數點後面不需做處理直接串接
    if (len(postfix) > 0):
      resultList.append('.')
      resultList.append(postfix)

    return "".join(resultList)