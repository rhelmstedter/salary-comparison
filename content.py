from salary_comparison import MONTHLY_PREMIUMS

intro = """This dashboard displays the estimated lifetime earnings for several school districts in Ventura County, CA."""

details = """## Analysis Details

Currently the analysis includes the following schools:
+ Conejo Valley Unified School District (CVUSD)
+ Fillmore Unified School District (FUSD)
+ Hueneme Elementary School District (HESD)
+ Oak Park Unified School District (OPUSD)
+ Ocean View School District (OVSD)
+ Oxnard School District (OSD)
+ Oxnard Union High School District (OUHSD)
+ Pleasant Valley School District (PVSD)
+ Rio School District (RSD)
+ Santa Paula Unified School District (SPUSD)
+ Simi Valley Unified School District (SVUSD)
+ Ventura Unified School District (VUSD)

Every district is up to date as of 09/11/22.

Choosing a district to focus on from the drop-down menu highlights that district in the graphs and calculates the differences between all other districts. Choosing the minimum number of units and degree type held by a teacher changes the column used in the analysis according to the qualifications set by each district. Finally, you can select a proposed raise percentage to see how it will impact salary."""

benefits = """### Accounting for Benefits

Due to the variation in benefits, it is difficult construct a direct comparison. It is possible for individual employees to pay more or less than the figures indicated in the table below. E.g., in this analysis, OUHSD monthly premiums are estimated at $180, but employees who choose Kaiser do not contribute a monthly premium. On the other hand, OVSD monthly premiums are estimated at $350, but employees have the ability to choose a plan that has a $1000 monthly premium. Based on what I could find through conversations with people from other districts and searching through district websites, I have estimated the cost of health benefits for each district and sorted them by cost as follows:
"""

benefits_table = """| District | Monthly Premium |
| -------- | --------------: |
"""
sorted_premiums = dict(sorted(MONTHLY_PREMIUMS.items(), key=lambda d: d[1]))
for district, premium in sorted_premiums.items():
    benefits_table += f"|{district}|${premium}|\n"

diff_calcs = """### Calculating Lifetime Earnings Differences

The expected value of lifetime earnings is computed by calculating the average difference between the focus district and each other district (including both paying for and opting out of benefits) for a particular degree held and units earned by a teacher. A negative result indicates that a teacher earns that much less than teachers in other districts on average. A positive result indicates a teacher earns that much more on average.

To view the difference between each district, hover over the barchart. The lower bound represents the difference if the teacher pays a 12 month premium. The upper bound represents the difference if the teacher opts out of benefits or chooses a plan that is 100% funded by the respective district.
"""

outro = """## Sources and Corrections
The goal of this page is to provide concrete data on salary diffences across districts in Ventura County. The analysis is the result of converting salary schedules from `pdfs` to `csv` files (some of which were required to be typed out by hand). While I have tried to be as accurate as possible in the analysis, it is possible that I have made mistakes when transcribing salaries or in the various calculations. If anyone notices a mistake or has more accurate salary/benefit data please contact me at rhelmstedter@gmail.com. I will do my best to correct it as soon a possible.

All of the salary schedules are publicly available in PDF form from the respective district websites. They can also be found in both PDF and CSV form on the [github repo](https://github.com/rhelmstedter/salary-comparison). The code, including all the calculations in salary difference and expected lifetime earnings, is written in Python and freely available in the [github repo](https://github.com/rhelmstedter/salary-comparison)."""
