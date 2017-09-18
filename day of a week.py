def number(n):
    try:
        int(n)
        return True
    except BaseException:
        return False


print("1 Monday \n"
      "2 Tuesday \n"
      "3 Wednesday \n"
      "4 Thursday \n"
      "5 Friday \n"
      "6 Saturday \n"
      "7 Sunday")
a = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
     4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
n = input('Choose the day from list below ')
if number(n):
    n = int(n)
    if n in range(1, 7):
        print(a[n])
    else:
        print(n//7, 'weeks, and it is', a[n % 7])
else:
    print('Something wrong...')
