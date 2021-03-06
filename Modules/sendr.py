import requests
import time

thefile = {"ext": "res", "data": ["TITL znp3_a_a.res in P2(1)/c\n",
                                  "ao_znp3.res created by SHELXL-2016/5 at 17:58:59 on 17-May-2020\n",
                                  "CELL  0.65253   7.5400   7.2720   8.8440   90.000  102.308   90.000\n",
                                  "ZERR    4.000   0.0015   0.0014   0.0018    0.000    0.030    0.000\n", "LATT  1\n",
                                  "SYMM -X, 1/2+Y, 1/2-Z\n", "SFAC P ZN\n", "UNIT 12 4\n", "L.S. 10\n", "BOND\n", "",
                                  "SHEL 99 0.7\n", "SIZE 0.02 0.02 0.015\n", "LIST 6\n", "FMAP 2\n", "TEMP -173\n",
                                  "RIGU\n", "PLAN 20\n", "WGHT    0.068100    0.731200\n", "FVAR       0.34649\n",
                                  "ZN1   2    0.606808    0.403421    0.275072    11.00000    0.00368    0.01127 =\n",
                                  "0.02029    0.00007    0.00238    0.00078\n",
                                  "ZN2   2    0.080764    0.253017    0.393987    11.00000    0.00349    0.01048 =\n",
                                  "0.02013    0.00004    0.00236   -0.00006\n",
                                  "P1    1    0.242849    0.515347    0.427817    11.00000    0.00442    0.01057 =\n",
                                  "0.01888   -0.00001    0.00247    0.00009\n",
                                  "P2    1    0.235099    0.980341    0.440798    11.00000    0.00424    0.01039 =\n",
                                  "0.01923    0.00011    0.00233    0.00013\n",
                                  "P3    1    0.078677    0.743101    0.395602    11.00000    0.00365    0.01092 =\n",
                                  "0.01886   -0.00013    0.00196    0.00012\n",
                                  "P4    1    0.374356    0.572188    0.215883    11.00000    0.00408    0.01009 =\n",
                                  "0.01946    0.00006    0.00246    0.00080\n", "HKLF 4\n", "", "", "", "",
                                  "REM  znp3_a_a.res in P2(1)/c\n",
                                  "REM R1 =  0.0412 for    1311 Fo > 4sig(Fo)  and  0.0418 for all    1352 data\n",
                                  "REM     55 parameters refined using     30 restraints\n", "", "END  \n", "",
                                  "WGHT      0.0713      0.6479 \n", "",
                                  "REM Highest difference peak  1.999,  deepest hole -1.739,  1-sigma level  0.330\n",
                                  "Q1    1   0.6165  0.3871  0.3640  11.00000  0.05    2.00\n",
                                  "Q2    1   0.5906  0.4025  0.1827  11.00000  0.05    1.97\n",
                                  "Q3    1   0.0890  0.2560  0.4835  11.00000  0.05    1.93\n",
                                  "Q4    1   0.0694  0.2514  0.3020  11.00000  0.05    1.77\n",
                                  "Q5    1   0.2247  0.5313  0.3263  11.00000  0.05    0.91\n",
                                  "Q6    1   0.0665  0.7468  0.4939  11.00000  0.05    0.91\n",
                                  "Q7    1   0.3583  0.5489  0.3006  11.00000  0.05    0.90\n",
                                  "Q8    1   0.1133  0.8628  0.2486  11.00000  0.05    0.87\n",
                                  "Q9    1   0.3551  0.5100  0.3661  11.00000  0.05    0.83\n",
                                  "Q10   1   0.3745  1.0054  0.3955  11.00000  0.05    0.82\n",
                                  "Q11   1   0.2330  0.5094  0.5156  11.00000  0.05    0.80\n",
                                  "Q12   1   0.2331  0.9432  0.3394  11.00000  0.05    0.78\n",
                                  "Q13   1   0.0624  0.7389  0.3020  11.00000  0.05    0.75\n",
                                  "Q14   1   0.2177  0.9914  0.5340  11.00000  0.05    0.73\n",
                                  "Q15   1  -0.0998  0.6916  0.2976  11.00000  0.05    0.72\n",
                                  "Q16   1   0.7403  0.4115  0.2306  11.00000  0.05    0.71\n",
                                  "Q17   1   0.3701  0.6801  0.2214  11.00000  0.05    0.69\n",
                                  "Q18   1  -0.0541  0.2661  0.4462  11.00000  0.05    0.67\n",
                                  "Q19   1   0.3195  0.6381  0.1883  11.00000  0.05    0.67\n",
                                  "Q20   1   0.3680  0.2495  0.3240  11.00000  0.05    0.66\n"]}

while True:
   r = requests.post("http://localhost:8080", data=thefile)
   time.sleep(0.1)
   print(r.status_code, r.reason)