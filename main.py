


def future_value_annuity(payment, rate, periods):
    """
    Calculate the future value of an annuity

    :param payment: Payment per period
    :param rate: Interest rate per period 
    param periods: Number of periods
    :return: Future Value

    """
    return payment * (((1+r)**periods-1)/rate)



def present_value_annuity(payment, rate, periods):
    """
    Calculate the present value of an annuity

    :param payment: Payment per period
    :param rate: Interest rate per period (decimal)
    :param periods: Number of periods
    :return: Present Value
    """

    return payment * ((1-(1+rate)**-periods)/rate)



pmt = 1000
r= 0.05
n=10

fv = future_value_annuity(pmt,r,n)
pv = present_value_annuity(pmt,r,n)

print("Future Value of Annuity:",fv)
print("Present value of Annuity:", pv)
