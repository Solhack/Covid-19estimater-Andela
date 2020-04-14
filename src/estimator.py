
test_data = {"data":{
  "region" : {
    "name":"africa",
    "avgAge":19.7,
    "avgDailyIncomeInUSD":4,
    "avgDailyIncomePopulation":0.73,
  },
  "periodType":"days",
  "timeToElapse":38,
  "reportedCases":2747,
  "population":92931687,
  "totalHospitalBeds":678874,
}}



def estimator(data):
    _data = data
    data = data['data']
    numberOfDays = data["timeToElapse"]
    durationType = data["periodType"]
    reportedCases = data["reportedCases"]
    hospitalBeds = data["totalHospitalBeds"]
    income = data["region"]["avgDailyIncomeInUSD"]
    percentage = data["region"]["avgDailyIncomePopulation"]

    numberOfDays = daysConverter(numberOfDays, durationType)
    (
      currentlyInfected,
      severeCurrentlyInfected,
      requestedTime,
      requestedTimeSevere,
      severeCasesByRequestedTime,
      severeSevereCasesByRequestedTime,
      hospitalBedsLeft,
      severeHospitalBedsLeft,
      icuCases,
      severeIcuCases,
      ventilatorCases,
      severeVentilatorCases,
      dollarsInFlight,
      severeDollarsInFlight

    ) = impactAssess(reportedCases, numberOfDays, hospitalBeds, percentage, income)

    impact = {
      "currentlyInfected": currentlyInfected,
      "infectionsByRequestedTime": requestedTime,
      "severeCasesByRequestedTime": severeCasesByRequestedTime,
      "hospitalBedsByRequestedTime": hospitalBedsLeft,
      "casesForICUByRequestedTime": icuCases,
      "casesForVentilatorsByRequestedTime": ventilatorCases, 
      "dollarsInFlight": dollarsInFlight
    }

    severeImpact = {
      "currentlyInfected": severeCurrentlyInfected,
      "infectionsByRequestedTime": requestedTimeSevere,
      "severeCasesByRequestedTime": severeSevereCasesByRequestedTime,
      "hospitalBedsByRequestedTime": severeHospitalBedsLeft,
      "casesForICUByRequestedTime": severeIcuCases,
      "casesForVentilatorsByRequestedTime": severeVentilatorCases,
      "dollarsInFlight": severeDollarsInFlight
    }

    data = {}

    data["data"] = _data
    data["impact"] = impact
    data["severeImpact"] = severeImpact

    return data

    
def daysConverter(number, durationType):
    if durationType == 'days':
      days = number
    elif durationType == 'weeks':
      days = (days * 7)
    else:
      days = (days * 30)
    return days



def impactAssess(reportedCases, numberOfDays, hospitalBeds,percentage,income):
    """
      write what this function does as docstring
    """
    _hospitalBeds = hospitalBeds
    hospitalBeds = hospitalBeds * .35
    impact = reportedCases * 10
    severeImpact = reportedCases * 50
    impactTime = impact * ( 2 ** (numberOfDays//3))
    impactTimeSevere = severeImpact * ( 2 ** (numberOfDays//3))
    severeCasesByRequestedTime = int(impactTime *15/100)
    severeSevereCasesByRequestedTime = int(impactTimeSevere *15/100)
    hospitalBedsLeft = ( _hospitalBeds * .35 ) - severeCasesByRequestedTime
    severeHospitalBedsLeft = ( _hospitalBeds * .35 ) - severeSevereCasesByRequestedTime
    hospitalBedsLeft = int(hospitalBedsLeft)
    severeHospitalBedsLeft = int(severeHospitalBedsLeft)
    icuCases = int(( .05 * impactTime))
    severeIcuCases = int((.05 * impactTimeSevere))
    ventilatorCases = int(( .02 * impactTime))
    severeVentilatorCases = int((.02 * impactTimeSevere))
    dollarsInFlight = int((impactTime * income * percentage) / numberOfDays)
    severeDollarsInFlight = int((impactTimeSevere * income * percentage) / numberOfDays)

    return impact, severeImpact, impactTime, impactTimeSevere, severeCasesByRequestedTime, severeSevereCasesByRequestedTime, hospitalBedsLeft, severeHospitalBedsLeft, icuCases, severeIcuCases, ventilatorCases, severeVentilatorCases, dollarsInFlight, severeDollarsInFlight
    