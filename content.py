intro = """This dashboard displays the estimated lifetime earnings for several school districts in Ventura County, CA."""

analysis_text = """## Analysis
Choose a district to focus on from the drop-down menu. Then choose the minimum number of units and degree type held by a teacher. Finally, choose a percentage for proposed raise to see how it will impact salary."""

explanation = """## Details

Currently the analysis includes the following schools:
+ Conejo Valley Unified School District (CVUSD)
+ Fillmore Unified School District (FUSD)
+ Hueneme Elementary School District (HESD)
+ Ocean View School District (OVSD)
+ Oxnard School District (OSD)
+ Oxnard Union High School District (OUHSD)
+ Pleasant Valley School District (PVSD)
+ Rio School District (RSD)
+ Santa Paula Unified School District (SPUSD)
+ Simi Valley Unified School District (SVUSD)
+ Ventura Unified School District (VUSD)

Every district is up to date as of 09/02/22.

Due to the variation in benefits and qualifications for columns across districts, it is difficult construct a direct comparison. It is possible for individual employees to pay more or less than the figures indicated in the table below. E.g., in this analysis, OUHSD monthly premiums are estimated at $180, but employees who choose Kaiser do not contribute a monthly premium. On the other hand, OVSD monthly premiums are estimated at $350, but employees have the ability to choose a plan that has a $1000 monthly premium. Based on what I could find through conversations with people from other districts and searching through district websites, I have estimated the cost of health benefits for each district as follows:

| District | Monthly Premium |
| -------- | :-------------: |
| HESD     | 0               |
| VUSD     | 0               |
| OSD      | 130             |
| CVUSD    | 160             |
| OUHSD    | 180             |
| PVSD     | 200             |
| RSD      | 200             |
| SPUSD    | 250             |
| SVUSD    | 250             |
| FUSD     | 300             |
| OVSD     | 350             |

The expected value of lifetime earnings is computed by calculating the average difference between the focus district and each other district (including both paying for and opting out of benefits) for a particular degree held and units earned by a teacher. A negative result indicates that a teacher earns that much less than teachers in other districts on average. A positive result indicates a teacher earns that much more on average.
"""

outro = """## Notes
The analysis above is the result of converting salary schedules from `pdfs` to `csv` files (some of which were required to be typed out by hand). While I have tried to be as accurate as possible in my analysis, it is possible that I made a mistake when transcribing salaries, or in the various calculations included in the code. If anyone notices a mistake please contact me at rhelmstedter@gmail.com. I will do my best to correct it as soon a possible. All of the salary schedules are publicly available in PDF form from the respective district websites. They can also be found in both PDF and CSV form on the [github repo](https://github.com/rhelmstedter/salary-comparison). The code, including all the calculations in salary difference and expected lifetime earnings, is written in Python and freely available in the [github repo](https://github.com/rhelmstedter/salary-comparison)."""
