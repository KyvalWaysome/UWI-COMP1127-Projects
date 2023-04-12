def days_in_month(month):
    month_days = [('January',[31]),('February',[28,29]),('March',[31]),
('April',[30]),('May',[31]),('June',[30]),('July',[31]),('August',[31]),
('September',[30]),('October',[31]),('November',[30]),('December',[31])]#declare list with month
    for x in month_days:
        if x[0]== month:
            return x[1] #continue till december
    return []#where the given month is not found

def day_of_week(d, m, y):
  if m==1 or m==2:#january or February
    m = m+12 #increments m by 12 to get the next day of the month
    y=y-1 #subtract one from the year to calculating the day
  day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] #list of thenm
  day = (((13*m+3) // 5 + d + y + (y // 4) - (y // 100) + (y // 400)) %7)
  day=int(day) #coverts the result in an integer value
  return day_names[day]

def unlucky(yr):#returns all the days in the year which have the date friday13th
    return [(13,x,yr) for x in range(1,13) if day_of_week(13,x,yr)=='Friday']#if part checks if fri

def mostUnlucky(start_year, end_year):#list of unlucky dates for a year
    years=[unlucky(x) for x in range(start_year,end_year+1)]
    return [x[0][2] for x in years if len(x)>2]#length greater than two year is added to an list 
#uses back unlucky to get a list of unlucky dates for a particular year
