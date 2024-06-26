//Insert applications
print("Load applications");
db.application.insert({ "_id" : "sentilo-catalog", "_class" : "org.sentilo.web.catalog.domain.Application", "name" : "sentilo-catalog", "token" : "c956c302086a042dd0426b4e62652273e05a6ce74d0b77f8b5602e0811025066", "description" : "Catalog application", "email" : "sentilo@sentilo.org", "createdAt" : new ISODate(), "authorizedProviders" : [ ] , "active":true });

// Insert users
print("Load users");
// db.user.insert({ "_id" : "admin", "_class" : "org.sentilo.web.catalog.domain.User", "password" : "1234", "name" : "Administrador", "description" : "", "email" : "sentilo@sentilo.org", "createdAt" : new ISODate(), "active" : true, "roles" : [ "ADMIN"] });
db.user.insert({ "_id" : "platform_user", "_class" : "org.sentilo.web.catalog.domain.User", "password" : "sentilo", "name" : "Platform user", "description" : "PubSub platform user. Do not remove  it!.", "email" : "sentilo@sentilo.org", "createdAt" : new ISODate(), "active" : true, "roles" : [ "PLATFORM" ] });

// Insert permissions
print("Load permissions");
db.permission.insert({ "_id" : "sentilo-catalog@sentilo-catalog", "_class" : "org.sentilo.web.catalog.domain.Permission", "source" : "sentilo-catalog", "target" : "sentilo-catalog", "type" : "ADMIN" });

//Create a default tenant with default params (name Sentilo, location centered at Barcelona, ...)
print("Load default tenant");
db.tenant.insert({ "_id" : "toledo-pr", "_class" : "org.sentilo.web.catalog.domain.Tenant", "name" : "Toledo", "description" : "Toledo tenant (default)", "isDefault": true, "contactName" : "Fill in your contact details", "contactEmail" : "fill_in@your.mail", "isPublic" : true, "mapParams" : { "zoomLevel" : 14, "center" : { "latitude" : -24.7300557, "longitude" : -53.7358805}, "bgColor" : "#1a671b"}, "createdAt" : new ISODate(), "createdBy" : "sadmin"});
db.tenant.insert({ "_id" : "vitoria-es", "_class" : "org.sentilo.web.catalog.domain.Tenant", "name" : "Vitória", "description" : "Vitória tenant", "isDefault": false, "contactName" : "Fill in your contact details", "contactEmail" : "fill_in@your.mail", "isPublic" : true, "mapParams" : { "zoomLevel" : 14, "center" : { "latitude" : -20.2841786, "longitude" : -40.3105601 }, "bgColor" : "#9a9a9a" }, "createdAt" : new ISODate(), "createdBy" : "sadmin"});

// Create a default super admin user 
print("Load default super-admin user");
db.user.insert({ "_id" : "sadmin", "_class" : "org.sentilo.web.catalog.domain.User", "password" : "change_it", "name" : "SuperAdmin user", "description" : "SuperAdmin user.", "email" : "fill_in@your.mail", "createdAt" : new ISODate(), "active" : true, "roles" : [  "SUPER_ADMIN" ] });