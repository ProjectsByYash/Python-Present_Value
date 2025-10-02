import warnings


def future_value_annuity(payment, rate, periods):
    """
    Calculate the future value of an annuity

    :param payment: Payment per period
    :param rate: Interest rate per period 
    param periods: Number of periods
    :return: Future Value

    """

    if payment <=0:
        warnings.warn("Payment should be positive. Did you mean to use a negative cash flow?")
    if periods <=0:
        raise ValueError("Number of periods must be greater than 0.")
    if rate == 0:
        return payment * periods #no interest case

    return payment * (((1+r)**periods-1)/rate)



def present_value_annuity(payment, rate, periods):
    """
    Calculate the present value of an annuity

    :param payment: Payment per period
    :param rate: Interest rate per period (decimal)
    :param periods: Number of periods
    :return: Present Value
    """

    if payment <=0:
        warnings.warn("Payment should be positive. Did you mean to use a negative cash flow?")
    if periods <=0:
        raise ValueError("Number of periods must be greater than 0.")
    if rate == 0:
        return payment * periods #no discounting case


    return payment * ((1-(1+rate)**-periods)/rate)



pmt = 1000
r= 0.0
n=10

fv = future_value_annuity(pmt,r,n)
pv = present_value_annuity(pmt,r,n)

print("Future Value of Annuity:",fv)
print("Present value of Annuity:", pv)
