def estimator(data):
    data = data
    numberOfDays = data["timeToElapse"]
    durationType = data["periodType"]
    reportedCases = data["reportedCases"]
    hospitalBeds = data["totalHospitalBeds"]
    income = data["region"]["avgDailyIncomeInUSD"]
    percentage = data["region"]["avgDailyIncomePopulation"]
    
def daysConverter(number, durationType):
  data == data
  if data["periodType"] == 'days':
    days = data["timeToElapse"]
  elif data["periodType"] == 'weeks':
    days = ((data["timeToElapse"]) * 7)
  else:
    days = ((data["timeToElapse"]) * 30)
  return days

def impactAssess(reportedCases, numberOfDays, hospitalBeds):
  hospitalBeds = hospitalBeds * .35
  impact = reportedCases * 10
  severeImpact = reportedCases * 50
  impactTime = impact * ( 2 ** (numberOfDays//3))
  impactTimeSevere = severeImpact * ( 2 ** (numberOfDays//3))
  severeCasesByRequestedTime = int(impactTime *15/100)
  severeSevereCasesByRequestedTime = int(impactTimeSevere *15/100)
  hospitalBedsLeft = ( data["totalHospitalBeds"] * .35 ) - severeCasesByRequestedTime
  severeHospitalBedsLeft = ( data["totalHospitalBeds"] * .35 ) - severeSevereCasesByRequestedTime
  hospitalBedsLeft = int(hospitalBedsLeft)
  severeHospitalBedsLeft = int(severeHospitalBedsLeft)
  icuCases = int(( .05 * impactTime))
  severeIcuCases = int((.05 * impactTimeSevere))
  ventilatorCases = int(( .02 * impactTime))
  severeVentilatorCases = int((.02 * impactTimeSevere))
  dollarsInFlight = int((impactTime * income * percentage) / numberOfDays)
  severeDollarsInFlight = int((impactTimeSevere * income * percentage) / numberOfDays)

  return impact, severeImpact, impactTime, impactTimeSevere, severeCasesByRequestedTime, severeSevereCasesByRequestedTime, hospitalBedsLeft, severeHospitalBedsLeft, icuCases, severeIcuCases, ventilatorCases, severeVentilatorCases, dollarsInFlight, severeDollarsInFlight

  numberOfDays = daysConverter(numberOfDays, durationType)
  currentlyInfected, severeCurrentlyInfected, requestedTime, requestedTimeSevere, severeCasesByRequestedTime, severeSevereCasesByRequestedTime, hospitalBedsLeft, severeHospitalBedsLeft, icuCases, severeIcuCases, ventilatorCases, severeVentilatorCases, dollarsInFlight, severeDollarsInFlight = impactAssess(reportedCases, numberOfDays, hospitalBeds)

  data = {}

  dataAndela = data

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

  data["data"] = dataAndela
  data["impact"] = impact
  data["severeImpact"] = severeImpact

  return data

