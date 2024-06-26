// Script with the minimum data to run the test process: application, providers, permissions, sensor and component types.
// Beware: init_data.js must be executed before run this script

//Insert applications
print("Load applications");
db.application.insert({ "_id" : "testApp", "_class" : "org.sentilo.web.catalog.domain.Application", "name" : "testApp", "token" : "646967a9f99ae76cfb836026d0015c4b80f8c0e1efbd3d261250156efd8fb96f", "description" : "Platform test app", "email" : "sentilo@sentilo.org", "createdAt" : ISODate("2013-02-22T10:20:19.963Z"), "authorizedProviders" : [ ] , "active":true});

// Insert providers
print("Load providers");
db.provider.insert({ "_id" : "testApp_provider", "_class" : "org.sentilo.web.catalog.domain.Provider", "name" : "testApp_provider", "token" : "563093ec5252147edc8860c2d667be5db0c010325b6953ed5b323724bcc00e05", "description" : "Provider to do APP integration tests", "createdAt" : ISODate("2013-03-15T08:48:42.966Z"), "contact" : { "name" : "Sentilo", "email" : "sentilo@sentilo.org" }, "active":true});
db.provider.insert({ "_id" : "testApi_provider", "_class" : "org.sentilo.web.catalog.domain.Provider", "name" : "testApi_provider", "token" : "595264c5bc8347adbadcd78249cc5809706782ce12a4501bbdf9e35a6da40164", "description" : "Provider to do API integration tests", "createdAt" : ISODate("2013-03-15T08:48:42.966Z"), "contact" : { "name" : "Sentilo", "email" : "sentilo@sentilo.org" }, "active":true});

// Insert alerts
print("Load alerts");
db.alert.insert({ "_id" : "testAlert", "_class" : "org.sentilo.web.catalog.domain.Alert", "name" : "testAlert", "description" : "Alert to do integration tests. Do not remove.", "createdAt" : ISODate("2015-05-18T10:49:23.438Z"), "type" : "EXTERNAL", "providerId" : "testApp_provider", "active" : true })

// Insert permissions
print("Load permissions");
db.permission.insert({ "_id" : "testApp_provider@testApp_provider", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "testApp_provider", "target" : "testApp_provider", "type" : "ADMIN" });
db.permission.insert({ "_id" : "testApi_provider@testApi_provider", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "testApi_provider", "target" : "testApi_provider", "type" : "ADMIN" });
db.permission.insert({ "_id" : "sentilo-catalog@testApp_provider", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "sentilo-catalog", "target" : "testApp_provider", "type" : "ADMIN" });
db.permission.insert({ "_id" : "sentilo-catalog@testApi_provider", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "sentilo-catalog", "target" : "testApi_provider", "type" : "ADMIN" });
db.permission.insert({ "_id" : "sentilo-catalog@testApp", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "sentilo-catalog", "target" : "testApp", "type" : "ADMIN" });
db.permission.insert({ "_id" : "testApp@testApp_provider", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "testApp", "target" : "testApp_provider", "type" : "READ" });
db.permission.insert({ "_id" : "testApp@testApi_provider", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "testApp", "target" : "testApi_provider", "type" : "READ" });
db.permission.insert({ "_id" : "testApp@testApp", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "testApp", "target" : "testApp", "type" : "ADMIN" });

// Insert component types
print("Load component types");
db.componentType.insert({ "_id" : "generic", "_class" : "org.sentilo.web.catalog.domain.ComponentType", "name" : "Generic", "description" : "Generic component type", "icon" : "pins1", "createdAt" : ISODate("2013-11-08T10:28:01.226Z") });
db.componentType.insert({ "_id" : "electricity_meter", "_class" : "org.sentilo.web.catalog.domain.ComponentType", "name" : "Electricity meter", "icon" : "pins2", "createdAt" : ISODate("2013-11-08T10:28:01.226Z") });
db.componentType.insert({ "_id" : "noise", "_class" : "org.sentilo.web.catalog.domain.ComponentType", "name" : "Noise meter", "icon" : "pins3", "createdAt" : ISODate("2013-11-08T10:28:01.226Z") });
db.componentType.insert({ "_id" : "meteo", "_class" : "org.sentilo.web.catalog.domain.ComponentType", "name" : "Meteo", "icon" : "pins4", "createdAt" : ISODate("2013-11-08T10:28:01.226Z") });
db.componentType.insert({ "_id" : "air_quality", "name" : "Air Quality", "description" : "Air Quality control", "icon" : "air", "createdAt" : ISODate("2023-09-27T12:41:24.125Z"), "_class" : "org.sentilo.web.catalog.domain.ComponentType" });
db.componentType.insert({ "_id" : "temperature", "name" : "Temperature", "description" : "Temperatura", "icon" : "temperatura", "createdAt" : ISODate("2023-09-27T12:44:59Z"), "_class" : "org.sentilo.web.catalog.domain.ComponentType" });
db.componentType.insert({ "_id" : "humidity", "name" : "Humidity", "description" : "Umidade", "icon" : "sky_spot", "createdAt" : ISODate("2023-09-27T12:50:34Z"), "_class" : "org.sentilo.web.catalog.domain.ComponentType" });
db.componentType.insert({ "_id" : "wind", "name" : "Anemometer", "description" : "Wind speed", "icon" : "ambient", "createdAt" : ISODate("2023-09-27T17:07:11.035Z"), "_class" : "org.sentilo.web.catalog.domain.ComponentType" });
db.componentType.insert({ "_id" : "traffic", "name" : "Traffic", "description" : "Traffic measurement", "icon" : "bus", "createdAt" : ISODate("2023-11-01T18:07:32.453Z"), "_class" : "org.sentilo.web.catalog.domain.ComponentType" })
// Insert sensor types
print("Load sensor types");
db.sensorType.insert({ "_id" :"temperature", "_class" : "org.sentilo.web.catalog.domain.SensorType", "name" : "Temperature",  "createdAt" : ISODate("2013-11-08T10:27:36.152Z") });
db.sensorType.insert({ "_id" :"noise", "_class" : "org.sentilo.web.catalog.domain.SensorType", "name" : "Noisemeter",  "createdAt" : ISODate("2013-11-08T10:27:36.152Z") });
db.sensorType.insert({ "_id" :"anemometer", "_class" : "org.sentilo.web.catalog.domain.SensorType", "name" : "Anenometer",  "createdAt" : ISODate("2013-11-08T10:27:36.152Z") });
db.sensorType.insert({ "_id" :"humidity", "_class" : "org.sentilo.web.catalog.domain.SensorType", "name" : "Humidity",  "createdAt" : ISODate("2013-11-08T10:27:36.152Z") });
db.sensorType.insert({ "_id" :"pluviometer", "_class" : "org.sentilo.web.catalog.domain.SensorType", "name" : "Pluviometer",  "createdAt" : ISODate("2013-11-08T10:27:36.152Z") });
db.sensorType.insert({ "_id" :"rain", "_class" : "org.sentilo.web.catalog.domain.SensorType", "name" : "Rain", "createdAt" : ISODate("2013-11-08T10:27:36.152Z") });
db.sensorType.insert({ "_id" :"wind", "_class" : "org.sentilo.web.catalog.domain.SensorType", "name" : "Wind",  "createdAt" : ISODate("2013-11-08T10:27:36.152Z") });
db.sensorType.insert({ "_id" : "air_quality_pm10", "name" : "PM10", "description" : "", "createdAt" : ISODate("2023-08-30T17:20:34.264Z"), "_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "air_quality_pm25", "name" : "PM25", "description" : "", "createdAt" : ISODate("2023-08-30T17:20:39.892Z"), "_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "air_quality_no2", "name" : "NO2", "description" : "Nitrogen dioxide measurement", "createdAt" : ISODate("2023-09-27T17:57:38.565Z"), "_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "air_quality_pm1", "name" : "PM1", "description" : "Measurement of suspension particles PM1", "createdAt" : ISODate("2023-09-27T17:58:08.401Z"),"_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "air_quality_o3", "name" : "O3", "description" : "Ozone measurement", "createdAt" : ISODate("2023-09-27T17:58:24.284Z"),"_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "air_quality_so2", "name" : "SO2", "description" : "Sulfur dioxide measurement", "createdAt" : ISODate("2023-09-27T17:58:39.072Z"), "_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "air_quality_co", "name" : "CO", "description" : "Carbon Monoxide measurement", "createdAt" : ISODate("2023-09-27T17:58:53.729Z"), "_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "air_quality_co2", "name" : "CO2", "description" : "Carbon dioxide measurement", "createdAt" : ISODate("2023-09-27T17:59:08.050Z"), "_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "air_quality_ox", "name" : "OX", "description" : "OX = O3 + NO2", "createdAt" : ISODate("2023-09-27T21:04:40.555Z"), "_class" : "org.sentilo.web.catalog.domain.SensorType" });
db.sensorType.insert({ "_id" : "tracker", "name" : "Tracker", "description" : "Vehicle tracker", "createdAt" : ISODate("2023-11-01T18:08:01.927Z"), "_class" : "org.sentilo.web.catalog.domain.SensorType" })