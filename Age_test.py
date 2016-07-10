x = int(input ("Input your year of birth (in 4 digits):_____"))
y = 2016 - x
if y < 18:
    print ("You're too YOUNG - TAKE A HIKE")
elif y<60:
    print ('Use moderation while consumming alchohol')
else:
    print ("You're an old ALCHOHOLIC! GO HOME!")
    