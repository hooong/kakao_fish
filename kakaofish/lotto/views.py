from django.shortcuts import render
import random

def start_btn(request):
    return render(request, 'start_btn.html')

def get_number(request):
    nums = []
    order = ['A', 'B', 'C', 'D', 'E']
    
    for _ in range(5):
        tmp = []
        cnt = 0
        while cnt != 6:
            tmp_num = random.randrange(1,46)
            if not tmp_num in tmp:
                tmp.append(tmp_num)
                cnt += 1
        nums.append(tmp)
    
    get_num = zip(order, nums)


    context = {'nums':get_num}
    return render(request, 'show_number.html', context)