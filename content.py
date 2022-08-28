intro = """This dashboard displays a salary comparison for the following school districts in Ventura county.
+ Hueneme Elementary School District (HESD)
+ Ocean View School District (OVSD)
+ Oxnard Union High School District (OUHSD)
+ Oxnard School District (OSD)
+ Pleasant Valley School District (PVSD)
+ Rio School District (RSD)
+ Santa Paula Unified School District (SPUSD)
+ Simi Valley Unified School District (SVUSD)
+ Ventura Unified School District (VUSD)

Every district is up to date as of 08/20/22 with the exception of SPUSD (which agreed to a 9% increase but has not released the new salary scale yet).

Due to the variation in benefits and qualifications for columns across districts, it is difficult to get a straight comparison. It is possible for individual employees to pay more or less than the figures indicated in the table below. E.g., OUHSD employees who choose Kaiser do not have a monthly premium while OVSD employees have the ability to choose a plan that has a $1000 monthly premium. Based on what I could find through conversations with people from other districts and searching through district websites, I have estimated health benefits costs as follows:

| District | Monthly Premium |
|----------|:---------------:|
| HESD     | 0               |
| OVSD     | 350             |
| OUHSD    | 180             |
| OSD      | 130             |
| PVSD     | 200             |
| RSD      | 200             |
| SPUSD    | 250             |
| SVUSD    | 250             |
| VUSD     | 0               |
"""

analysis_text = """## Analysis\nChoose a district to focus on from the dropdown menu. Then choose the number of units and degree type. You can also see how a proposed raise will impart salary moving forward. The differences in salary across a 36 year career are computed and displayed below the graph."""

outro = """## Notes
The analysis above is the result of converting salary schedules from pdfs to csv files (some of which I have had to type out by hand). While I have tried to be as accurate as possible in my analysis, it is possible that I made a mistake when transcribing salaries, or in the calculations included in the code. If anyone notices a mistake please let me know at rhelmstedter@gmail.com. I will do my best to correct it as soon a possible. All of the salary schedules are publically available in PDF form from the respective district webites. They can also be found in PDF and CSV on the [github repo](https://github.com/rhelmstedter/salary-comparison) I have put togther."""
