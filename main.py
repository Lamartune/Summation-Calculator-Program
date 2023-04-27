# /*
#  * * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#  * *
#  * * Copyright (C) 2023 Fatih Tün - All Rights Reserved
#  * *
#  * * Unauthorized copying of this file, via any medium is strictly prohibited
#  * *
#  * * Proprietary and confidental.
#  * *
#  * * Written by Fatih TÜN <tunbusiness1@gmail.com>, April 2023
#  */



num = int(input("Enter an integer number: "))

sum = 0
for i in range(1, num+1):
    sum += i

print("The summation of 1 to", num, "is:", sum)