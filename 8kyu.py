def duty_free(price, discount, holiday_cost):
    newprice = discount * 0.01 #ვითვლით ფასდაკლებას
    #ეს არის holiday VIII duty free
    
    
    bottleprice = price * newprice #რა იქნება ფასი ფასდაკლების შემდგომ
    
    return int(holiday_cost //  bottleprice) #საბოლოო ფასი
        