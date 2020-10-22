'''
medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

print(instructions)
'''

a='nam'
b=19
c='cse'
inst='{} is {} and is studying {} branch'.format(a,b,c)
print(inst)
inst='{1} years {0} studies in {2} branch'.format(a,b,c)
print(inst)
inst='{b} years {a} studies {c}'.format(a='nam',b=19,c='cs')
print(inst)
