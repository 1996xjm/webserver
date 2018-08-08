from django.conf.urls import url

from views import *
urlpatterns = [
    url(r'^nihao$', nihao),
    url(r'^addtrainee$', addTrainee),
    url(r'^deletetrainee$', deleteTrainee),
    url(r'^addattenceinfor$', addAttenceInfor),
    url(r'^getcheckinfor$', getcheckinfor),
    url(r'^setchinablueuserinfor$',setchinablueuserinfor),
    url(r'^getopenid$',getopenid),
    url(r'^findopenid$',findopenid),
    url(r'^getchinablueuser$',getchinablueuser),
    url(r'^addlunchuser$',addlunchuser),
    url(r'^addlunchinfor$',addlunchinfor),
    url(r'^getlunchuser$',getlunchuser),
    url(r'^getlunchinfor$',getlunchinfor),
    url(r'^getlunchexcel$',getlunchexcel),
    url(r'^deletelunchuser$',deletelunchuser),
    url(r'^saveformid$',saveformid),
    url(r'^sendworkcheckmsg$',sendworkcheckmsg),
    url(r'^templatetest$',templatetest),
    url(r'^gettraineename$',gettraineename)
]
