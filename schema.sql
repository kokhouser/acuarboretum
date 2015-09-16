drop table if exists plants;
create table plants(
	id integer primary key autoincrement,
	tesv money,
	structuralValue money,
	spCode varchar,
	genus varchar,
	commonName varchar,
	latinName varchar,
	dbh int,
	dbhRange varchar,
	treeHeightRange varchar,
	numStems int,
	priMainNeed varchar,
	secMainNeed varchar,
	furtherInspectNeed int,
	clearanceNeed varchar,
	pruneType varchar,
	pests varchar,
	observations varchar,
	notes varchar
	nearestBuilding varchar,
	directionToBuilding varchar,
	addressNum varchar,
	streetName varchar,
	overheadUtillities varchar,
	longitude real,
	latitude real,
	plantDate date
);