#Sistema de Ecuaciones
def px(a, b):
    if a < 0:
        b = b/ -a
        print("x={}".format(float(b * -1)))
    else:
        b = b / a
        print("x={}".format(float(b)))


def py(a, b):
    if a < 0:
        b = b / -a
        print("y={}".format(float(b * -1)))
    else:
        b = b / a
        print("y={}".format(float(b)))


def rpx(ec1, ec2, d):
    ec2 = [ec2[0] * d, ec2[1] * d, ec2[2] * d]
    if d < 0:
        r = [ec1[0] + ec2[0], ec1[1] + ec2[1], ec1[2] + ec2[2]]
    else:
        r = [ec1[0] - ec2[0], ec1[1] - ec2[1], ec1[2] - ec2[2]]
    px(r[0], r[2])


def rnx(ec1, ec2, d):
    ec1 = [ec1[0] * d, ec1[1] * d, ec1[2] * d]
    if d < 0:
        r = [ec1[0] + ec2[0], ec1[1] + ec2[1], ec1[2] + ec2[2]]
    else:
        r = [ec1[0] - ec2[0], ec1[1] - ec2[1], ec1[2] - ec2[2]]
    px(r[0], r[2])


def rpy(ec1, ec2, d):
    ec2 = [ec2[0] * d, ec2[1] * d, ec2[2] * d]
    if d < 0:
        r = [ec1[0] + ec2[0], ec1[1] + ec2[1], ec1[2] + ec2[2]]
    else:
        r = [ec1[0] - ec2[0], ec1[1] - ec2[1], ec1[2] - ec2[2]]
    py(r[1], r[2])


def rny(ec1, ec2, d):
    ec1 = [ec1[0] * d, ec1[1] * d, ec1[2] * d]
    if d < 0:
        r = [ec1[0] + ec2[0], ec1[1] + ec2[1], ec1[2] + ec2[2]]
    else:
        r = [ec1[0] - ec2[0], ec1[1] - ec2[1], ec1[2] - ec2[2]]
    py(r[1], r[2])


n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())
ec1 = [n1 * 2, n2 * 2, n3 * 2]
ec2 = [n4 * 2, n5 * 2, n6 * 2]
dif = ec1[1] / ec2[1]
if dif >= 0:
    rpx(ec1, ec2, dif)
else:
    rnx(ec1, ec2, dif)
dif = ec1[0] / ec2[0]
if dif >= 0:
    rpy(ec1, ec2, dif)
else:
    rny(ec1, ec2, dif)