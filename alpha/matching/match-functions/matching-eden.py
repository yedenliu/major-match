
# ------------------------------------------------------------------------------
# Import Modules
# ------------------------------------------------------------------------------
from matching_helpers import *


def masterCheck(userInput):
    majorsToCheck = get_majors(userInput)
    print(majorsToCheck)
    if 'History' in majorsToCheck:
        pass

# ------------------------------------------------------------------------------
# Testing
# ------------------------------------------------------------------------------
a = ['AFR 204', 'AFR 204', 'ARTH 237', 'ARTH 226', 'ARTH 244', 'ARTH 247', 'ARTH 317', 'ARTH 222', 'ARTH 309', 'ARTH 256', 'ARTH 335', 'CHEM 335', 'CHEM 341', 'CHEM 325', 'CHEM 335', 'ENG 311', 'ENG 382', 'ES 201', 'HIST 213', 'SOC 322', 'HIST 256', 'HIST 231', 'AFR 209', 'ARTH 307', 'SPAN 303', 'SPAN 377', 'HIST 215', 'ARTH 201']
b = ['CS 230', 'CS 235', 'CS 232', 'CS 323', 'CS 232', 'CS 235', 'CHIN 382', 'JPN 232', 'ARTH 240', 'KOR 232', 'CHIN 243', 'KOR 209H', 'FREN 324', 'MATH 370', 'MATH 313', 'MATH 306', 'MATH 223', 'STAT 318', 'MATH 207Y', 'MATH 250', 'MATH 313', 'MATH 313', 'ARTS 365', 'ARTS 350', 'ARTS 207', 'ARTS 165', 'SOC 220', 'PEAC 240', 'REL 233', 'JWST 201']
c = ['AFR 204', 'AFR 235', 'ARTS 222', 'SOC 314', 'ARTH 240', 'ARTH 318', 'POL1 333', 'CAMS 234', 'CAMS 238', 'CAMS 228', 'CAMS 234', 'SPAN 268', 'CAMS 228', 'FREN 300', 'ARTS 208', 'CAMS 219', 'BISC 198', 'CS 230', 'BISC 198', 'CS 232', 'QR 260', 'GER 350', 'HIST 376', 'CAMS 201', 'MAS 222', 'CAMS 233', 'MUS 275', 'SPAN 269', 'WGST 214', 'WGST 360']
d = ['MUS 250', 'CS 230', 'AMST 152', 'GER 389', 'STAT 318', 'CS 343', 'CS 304', 'MUS 309', 'GER 225', 'GER 386', 'AMST 215', 'JPN 251', 'GER 350H', 'PHYS 350H', 'GER 286', 'SWA 203', 'ENG 342', 'FREN 300', 'GER 250H', 'AFR 212', 'ENG 234', 'GER 229', 'CHIN 204', 'THST 251', 'CS 315', 'PHYS 323H', 'CHIN 320', 'GER 239', 'HIST 204', 'GER 370']
e = ['PHYS 355', 'AMST 231', 'ASTR 303', 'LING 246', 'RUSS 386H', 'PSYC 216', 'CS 235', 'AFR 303', 'CS 111', 'AFR 211', 'ASTR 311', 'AFR 380', 'AFR 306', 'PHYS 360', 'EALC 225', 'PHYS 302', 'AFR 206', 'ENG 210', 'SWA 201', 'CS 232', 'ARTH 255', 'AFR 204', 'HIST 213', 'JPN 352', 'AFR 318', 'CS 230', 'CS 220']
f = ['SPAN 287', 'MATH 302', 'MATH 340', 'LING 238', 'CHEM 350', 'AFR 302', 'HIST 268', 'HIST 369', 'PHYS 350', 'SWA 203', 'PHYS 355', 'AFR 380', 'PHIL 207', 'MATH 307', 'SPAN 250', 'AFR 341', 'MATH 313', 'MATH 365', 'MATH 325', 'MATH 350', 'SPAN 291', 'MATH 310', 'SPAN 293', 'PSYC 216', 'PHYS 365', 'MATH 215', 'PHYS 305', 'PHYS 370']
g = ['AFR 207', 'ENG 213', 'ECON 327', 'REL 345', 'JWST 209', 'CAMS 241', 'CAMS 366', 'ENG 349', 'JWST 245', 'JWST 270', 'MUS 336', 'JWST 201', 'CAMS 235', 'MAS 250H', 'WRIT 120', 'REL 227', 'JWST 345', 'CAMS 250', 'CHEM 350H', 'ENG 211', 'FREN 330', 'JWST 233', 'SAS 302', 'ENG 222', 'JWST 350H']
h = ['ITAS 263', 'REL 318', 'ITAS 202', 'ENG 268', 'ITAS 210', 'SAS 303', 'REL 225', 'ITAS 261', 'ENG 208', 'ENG 260', 'ITAS 271', 'ITAS 270', 'FREN 303', 'HIST 260', 'PHIL 245', 'ITAS 203', 'FREN 205', 'SAS 350', 'ENG 311', 'SAS 302', 'ITAS 274', 'FREN 241', 'PEAC 215', 'POL4 340', 'ENG 210', 'SAS 242', 'PEAC 360', 'FREN 207']
i = ['PEAC 225', 'AFR 204', 'PEAC 243', 'ENG 295', 'PEAC 370', 'THST 360', 'POL1 210', 'AFR 350', 'PHYS 350H', 'PEAC 290', 'PEAC 210', 'PHYS 304', 'PEAC 240', 'AFR 206', 'PEAC 206', 'PHYS 370', 'PEAC 388', 'PEAC 205', 'AFR 216', 'ECON 334', 'WGST 250H', 'PHYS 355', 'GER 250H', 'HIST 273', 'PEAC 235', 'AFR 215', 'PEAC 224']
j = ['CS 112', 'POL3 351', 'PEAC 206', 'HIST 221', 'SOC 312', 'PEAC 261', 'MATH 313', 'HIST 280', 'POL1 210', 'PEAC 264', 'PSYC 345', 'ECON 312', 'MATH 314', 'ECON 214', 'PSYC 217', 'PEAC 201', 'CLSC 316', 'PSYC 301', 'STAT 228', 'PSYC 216', 'PEAC 207/', 'POL2 362', 'POL1 333', 'LAT 308', 'PSYC 215', 'WGST 215', 'PSYC 315R']
k = ['ECON 101','ECON 203','ECON 222','EDUC 226','ECON 233','ECON 314','ECON 318','ECON 320','CS 242','CS 301','CS 304','CS 342','FREN 101','FREN 102','FREN 201','FREN 202','HIST 245','HIST 220','JPN 290','MATH 205','MATH 206','MATH 223','MATH 225','NEUR 100','PHIL 215','POL1 200','WRIT 166']

masterCheck(a)