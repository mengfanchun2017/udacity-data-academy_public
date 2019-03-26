import numpy as np

# First 20 countries with school completion data
countries = np.array([
      'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria','Azerbaijan',
      'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
      'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
      'Cambodia', 'Cameroon', 'Cape Verde'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
    98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
    95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
    29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
])

# # Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
     95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
     97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
    102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
     37.00692,   45.39401,   91.22084,   62.42028,   90.66958
])

def overall_completion_rate(female_completion, male_completion):
    '''
    Fill in this function to return a NumPy array containing the overall
    school completion rate for each country. The arguments are NumPy
    arrays giving the female and male completion of each country in
    the same order.
    '''
    whole_rate = (female_completion + male_completion)/2
    return whole_rate

print(overall_completion_rate(female_completion, male_completion))
print(type(overall_completion_rate(female_completion, male_completion)))
