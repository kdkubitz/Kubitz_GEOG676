part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
# multiply all items together
def func1(part1):
    ans1 = 1
    for num in part1:
        ans1 *= num
    print(ans1)
func1(part1)

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
# add all items together
def func2(part2):
    ans2 = 0
    for num in part2:
        ans2 += num
    print(ans2)
func2(part2)

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 1, 14, 38, 26, 21]
# add together only those that are even
def func3(part3):
    func3 = sum(num for num in part3 if num % 2 == 0)
    print(func3)
func3(part3)