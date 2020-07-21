#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. Sample ip 07:05:45PM
def timeConversion(s):

    if 'AM' in s:
        s = s.replace("AM","")
        if s[:2]== '12':
            return '00'+s[2:]
        else:
            return s
    if 'PM' in s:
        s = s.replace("PM","")
        if s[:2] == '12':
            return s
        else:
            return str(int(s[:2])+12)+s[2:]
