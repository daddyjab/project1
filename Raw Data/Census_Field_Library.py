census_aliases = {  
  ## Economic Variables 
    "income":{  
    "api":"acs",
    "variable":"B19013_001E",
    "description":"Median household income in the past 12 months (in 2013 inflation-adjusted dollars)",
    "text":"median household income",
    "unit":"dollars"
  },
  "income_per_capita":{  
    "api":"acs",
    "variable":"B19301_001E",
    "description":"Per capita income in the past 12 months (in 2013 inflation-adjusted dollars)",
    "text":"per capita income",
    "unit":"dollars"
  },
  ## Employment Status 
    "employment_labor_force":{  
    "api":"acs",
    "variable":"B23025_002E",
    "description":"Number of persons, age 16 or older, in the labor force",
    "text":"employable people in the labor force",
    "unit":"pop"
  },
  "employment_not_labor_force":{  
    "api":"acs",
    "variable":"B23025_007E",
    "description":"Number of persons, age 16 or older, not in the labor force",
    "text":"people outside of the labor force",
    "unit":"pop"
  },
  "employment_civilian_labor_force":{  
    "api":"acs",
    "variable":"B23025_003E",
    "description":"Number of persons, age 16 or older, in the civilian labor force",
    "text":"employable civilians",
    "unit":"pop"
  },
  "employment_employed":{  
    "api":"acs",
    "variable":"B23025_004E",
    "description":"Number of employed, age 16 or older, in the civilian labor force",
    "text":"employed civilians",
    "unit":"pop"
  },
  "employment_unemployed":{  
    "api":"acs",
    "variable":"B23025_005E",
    "description":"Number of unemployed, age 16 or older, in the civilian labor force",
    "text":"unemployed civilians",
    "unit":"pop"
  },
  "employment_armed_forces":{  
    "api":"acs",
    "variable":"B23025_006E",
    "description":"Number of persons, age 16 or older, in the Armed Forces",
    "text":"people in the military",
    "unit":"pop"
  },
  "employment_male_management_business_science_and_arts_occupations":{  
    "api":"acs",
    "variable":"C24010_003E",
    "description":"Number of employed male 'Management, business, science, or arts occupations:' for the civilian population age 16 and over",
    "text":"men who work in management, business, science, or the arts",
    "unit":"pop"
  },
  "employment_male_management_business_and_financial_occupations":{  
    "api":"acs",
    "variable":"C24010_004E",
    "description":"Number of employed male 'Management, business, or financial occupations:' for the civilian population age 16 and over",
    "text":"men who work in management, business, or finance",
    "unit":"pop"
  },
  "employment_male_management_occupations":{  
    "api":"acs",
    "variable":"C24010_005E",
    "description":"Number of employed male 'Management occupations' for the civilian population age 16 and over",
    "text":"men who work in management",
    "unit":"pop"
  },
  "employment_male_business_and_financial_operations_occupations":{  
    "api":"acs",
    "variable":"C24010_006E",
    "description":"Number of employed male 'Business and financial operations occupations' for the civilian population age 16 and over",
    "text":"men who work in business and financial operations",
    "unit":"pop"
  },
  "employment_male_computer_engineering_and_science_occupations":{  
    "api":"acs",
    "variable":"C24010_007E",
    "description":"Number of employed male 'Computer, engineering, or science occupations:' for the civilian population age 16 and over",
    "text":"men working in STEM fields",
    "unit":"pop"
  },
  "employment_male_computer_and_mathematical_occupations":{  
    "api":"acs",
    "variable":"C24010_008E",
    "description":"Number of employed male 'Computer and mathematical occupations' for the civilian population age 16 and over",
    "text":"men who work in computers and math",
    "unit":"pop"
  },
  "employment_male_architecture_and_engineering_occupations":{  
    "api":"acs",
    "variable":"C24010_009E",
    "description":"Number of employed male 'Architecture and engineering occupations' for the civilian population age 16 and over",
    "text":"men who work in architecture and engineering",
    "unit":"pop"
  },
  "employment_male_life_physical_and_social_science_occupations":{  
    "api":"acs",
    "variable":"C24010_010E",
    "description":"Number of employed male 'Life, physical, or social science occupations' for the civilian population age 16 and over",
    "text":"men who work in life, physical, or social sciences",
    "unit":"pop"
  },
  "employment_male_education_legal_community_service_arts_and_media_occupations":{  
    "api":"acs",
    "variable":"C24010_011E",
    "description":"Number of employed male 'Education, legal, community service, arts, or media occupations:' for the civilian population age 16 and over",
    "text":"men who work in education, legal, community service, arts, or media",
    "unit":"pop"
  },
  "employment_male_community_and_social_service_occupations":{  
    "api":"acs",
    "variable":"C24010_012E",
    "description":"Number of employed male 'Community and social service occupations' for the civilian population age 16 and over",
    "text":"men who work in community or social services",
    "unit":"pop"
  },
  "employment_male_legal_occupations":{  
    "api":"acs",
    "variable":"C24010_013E",
    "description":"Number of employed male 'Legal occupations' for the civilian population age 16 and over",
    "text":"men working in the legal field",
    "unit":"pop"
  },
  "employment_male_education_training_and_library_occupations":{  
    "api":"acs",
    "variable":"C24010_014E",
    "description":"Number of employed male 'Education, training, or library occupations' for the civilian population age 16 and over",
    "text":"men working in education",
    "unit":"pop"
  },
  "employment_male_arts_design_entertainment_sports_and_media_occupations":{  
    "api":"acs",
    "variable":"C24010_015E",
    "description":"Number of employed male 'Arts, design, entertainment, sports, or media occupations' for the civilian population age 16 and over",
    "text":"men working in arts, design, entertainment, media, or sports",
    "unit":"pop"
  },
  "employment_male_healthcare_practitioners_and_technical_occupations":{  
    "api":"acs",
    "variable":"C24010_016E",
    "description":"Number of employed male 'Healthcare practitioners and technical occupations:' for the civilian population age 16 and over",
    "text":"men working in healthcare",
    "unit":"pop"
  },
  "employment_male_health_diagnosing_and_treating_practitioners_and_other_technical_occupations":{  
    "api":"acs",
    "variable":"C24010_017E",
    "description":"Number of employed male 'Health diagnosing and treating practitioners and other technical occupations' for the civilian population age 16 and over",
    "text":"men working in health diagnosing and other medical occupations",
    "unit":"pop"
  },
  "employment_male_health_technologists_and_technicians":{  
    "api":"acs",
    "variable":"C24010_018E",
    "description":"Number of employed male 'Health technologists and technicians' for the civilian population age 16 and over",
    "text":"employed male health technicians",
    "unit":"pop"
  },
  "employment_male_service_occupations":{  
    "api":"acs",
    "variable":"C24010_019E",
    "description":"Number of employed male 'Service occupations:' for the civilian population age 16 and over",
    "text":"men working in the service industry",
    "unit":"pop"
  },
  "employment_male_healthcare_support_occupations":{  
    "api":"acs",
    "variable":"C24010_020E",
    "description":"Number of employed male 'Healthcare support occupations' for the civilian population age 16 and over",
    "text":"men who work in healthcare support",
    "unit":"pop"
  },
  "employment_male_protective_service_occupations":{  
    "api":"acs",
    "variable":"C24010_021E",
    "description":"Number of employed male 'Protective service occupations:' for the civilian population age 16 and over",
    "text":"men who work in protective services",
    "unit":"pop"
  },
  "employment_male_fire_fighting_and_prevention_and_other_protective_service_workers_including_supervisors":{  
    "api":"acs",
    "variable":"C24010_022E",
    "description":"Number of employed male 'Fire fighting and prevention, or other protective service workers including supervisors' for the civilian population age 16 and over",
    "text":"men working in protective services",
    "unit":"pop"
  },
  "employment_male_law_enforcement_workers_including_supervisors":{  
    "api":"acs",
    "variable":"C24010_023E",
    "description":"Number of employed male 'Law enforcement workers including supervisors' for the civilian population age 16 and over",
    "text":"men working in law enforcement",
    "unit":"pop"
  },
  "employment_male_food_preparation_and_serving_related_occupations":{  
    "api":"acs",
    "variable":"C24010_024E",
    "description":"Number of employed male 'Food preparation and serving related occupations' for the civilian population age 16 and over",
    "text":"men who work in food prep",
    "unit":"pop"
  },
  "employment_male_building_and_grounds_cleaning_and_maintenance_occupations":{  
    "api":"acs",
    "variable":"C24010_025E",
    "description":"Number of employed male 'Building and grounds cleaning and maintenance occupations' for the civilian population age 16 and over",
    "text":"male groundskeepers and building maintenance workers",
    "unit":"pop"
  },
  "employment_male_personal_care_and_service_occupations":{  
    "api":"acs",
    "variable":"C24010_026E",
    "description":"Number of employed male 'Personal care and service occupations' for the civilian population age 16 and over",
    "text":"men working in personal care",
    "unit":"pop"
  },
  "employment_male_sales_and_office_occupations":{  
    "api":"acs",
    "variable":"C24010_027E",
    "description":"Number of employed male 'Sales and office occupations:' for the civilian population age 16 and over",
    "text":"male office workers and sales associates",
    "unit":"pop"
  },
  "employment_male_sales_and_related_occupations":{  
    "api":"acs",
    "variable":"C24010_028E",
    "description":"Number of employed male 'Sales and related occupations' for the civilian population age 16 and over",
    "text":"men working in sales",
    "unit":"pop"
  },
  "employment_male_office_and_administrative_support_occupations":{  
    "api":"acs",
    "variable":"C24010_029E",
    "description":"Number of employed male 'Office and administrative support occupations' for the civilian population age 16 and over",
    "text":"male office administrators",
    "unit":"pop"
  },
  "employment_male_natural_resources_construction_and_maintenance_occupations":{  
    "api":"acs",
    "variable":"C24010_030E",
    "description":"Number of employed male 'Natural resources, construction, or maintenance occupations:' for the civilian population age 16 and over",
    "text":"men working in natural resource, construction, or maintenance",
    "unit":"pop"
  },
  "employment_male_farming_fishing_and_forestry_occupations":{  
    "api":"acs",
    "variable":"C24010_031E",
    "description":"Number of employed male 'Farming, fishing, or forestry occupations' for the civilian population age 16 and over",
    "text":"men who work in farming, fishing, or forestry",
    "unit":"pop"
  },
  "employment_male_construction_and_extraction_occupations":{  
    "api":"acs",
    "variable":"C24010_032E",
    "description":"Number of employed male 'Construction and extraction occupations' for the civilian population age 16 and over",
    "text":"male construction workers",
    "unit":"pop"
  },
  "employment_male_installation_maintenance_and_repair_occupations":{  
    "api":"acs",
    "variable":"C24010_033E",
    "description":"Number of employed male 'Installation, maintenance, or repair occupations' for the civilian population age 16 and over",
    "text":"male maintenance and repair workers",
    "unit":"pop"
  },
  "employment_male_production_transportation_and_material_moving_occupations":{  
    "api":"acs",
    "variable":"C24010_034E",
    "description":"Number of employed male 'Production, transportation, or material moving occupations:' for the civilian population age 16 and over",
    "text":"male factory, transit, or transportation workers",
    "unit":"pop"
  },
  "employment_male_production_occupations":{  
    "api":"acs",
    "variable":"C24010_035E",
    "description":"Number of employed male 'Production occupations' for the civilian population age 16 and over",
    "text":"male factory workers",
    "unit":"pop"
  },
  "employment_male_transportation_occupations":{  
    "api":"acs",
    "variable":"C24010_036E",
    "description":"Number of employed male 'Transportation occupations' for the civilian population age 16 and over",
    "text":"men who work in transit",
    "unit":"pop"
  },
  "employment_male_material_moving_occupations":{  
    "api":"acs",
    "variable":"C24010_037E",
    "description":"Number of employed male 'Material moving occupations' for the civilian population age 16 and over",
    "text":"men who work in transportation of physical goods",
    "unit":"pop"
  },
  "employment_female_management_business_science_and_arts_occupations":{  
    "api":"acs",
    "variable":"C24010_039E",
    "description":"Number of employed female 'Management, business, science, or arts occupations:' for the civilian population age 16 and over",
    "text":"women working in management, business, science, or the arts",
    "unit":"pop"
  },
  "employment_female_management_business_and_financial_occupations":{  
    "api":"acs",
    "variable":"C24010_040E",
    "description":"Number of employed female 'Management, business, or financial occupations:' for the civilian population age 16 and over",
    "text":"women working in management, business, or finance",
    "unit":"pop"
  },
  "employment_female_management_occupations":{  
    "api":"acs",
    "variable":"C24010_041E",
    "description":"Number of employed female 'Management occupations' for the civilian population age 16 and over",
    "text":"women managers",
    "unit":"pop"
  },
  "employment_female_business_and_financial_operations_occupations":{  
    "api":"acs",
    "variable":"C24010_042E",
    "description":"Number of employed female 'Business and financial operations occupations' for the civilian population age 16 and over",
    "text":"women working in business and finance",
    "unit":"pop"
  },
  "employment_female_computer_engineering_and_science_occupations":{  
    "api":"acs",
    "variable":"C24010_043E",
    "description":"Number of employed female 'Computer, engineering, or science occupations:' for the civilian population age 16 and over",
    "text":"women employed in STEM fields",
    "unit":"pop"
  },
  "employment_female_computer_and_mathematical_occupations":{  
    "api":"acs",
    "variable":"C24010_044E",
    "description":"Number of employed female 'Computer and mathematical occupations' for the civilian population age 16 and over",
    "text":"women working in computer science and math",
    "unit":"pop"
  },
  "employment_female_architecture_and_engineering_occupations":{  
    "api":"acs",
    "variable":"C24010_045E",
    "description":"Number of employed female 'Architecture and engineering occupations' for the civilian population age 16 and over",
    "text":"women working in architecture and engineering",
    "unit":"pop"
  },
  "employment_female_life_physical_and_social_science_occupations":{  
    "api":"acs",
    "variable":"C24010_046E",
    "description":"Number of employed female 'Life, physical, or social science occupations' for the civilian population age 16 and over",
    "text":"women who work in life, physical, or social sciences",
    "unit":"pop"
  },
  "employment_female_education_legal_community_service_arts_and_media_occupations":{  
    "api":"acs",
    "variable":"C24010_047E",
    "description":"Number of employed female 'Education, legal, community service, arts, or media occupations:' for the civilian population age 16 and over",
    "text":"women working in education, legal, community service, media, or the arts",
    "unit":"pop"
  },
  "employment_female_community_and_social_service_occupations":{  
    "api":"acs",
    "variable":"C24010_048E",
    "description":"Number of employed female 'Community and social service occupations' for the civilian population age 16 and over",
    "text":"women who work in community or social services",
    "unit":"pop"
  },
  "employment_female_legal_occupations":{  
    "api":"acs",
    "variable":"C24010_049E",
    "description":"Number of employed female 'Legal occupations' for the civilian population age 16 and over",
    "text":"women working in the legal field",
    "unit":"pop"
  },
  "employment_female_education_training_and_library_occupations":{  
    "api":"acs",
    "variable":"C24010_050E",
    "description":"Number of employed female 'Education, training, or library occupations' for the civilian population age 16 and over",
    "text":"women working in education",
    "unit":"pop"
  },
  "employment_female_arts_design_entertainment_sports_and_media_occupations":{  
    "api":"acs",
    "variable":"C24010_051E",
    "description":"Number of employed female 'Arts, design, entertainment, sports, or media occupations' for the civilian population age 16 and over",
    "text":"women who work in design, entertainment, sports, media, or the arts",
    "unit":"pop"
  },
  "employment_female_healthcare_practitioners_and_technical_occupations":{  
    "api":"acs",
    "variable":"C24010_052E",
    "description":"Number of employed female 'Healthcare practitioners and technical occupations:' for the civilian population age 16 and over",
    "text":"women working in healthcare",
    "unit":"pop"
  },
  "employment_female_health_diagnosing_and_treating_practitioners_and_other_technical_occupations":{  
    "api":"acs",
    "variable":"C24010_053E",
    "description":"Number of employed female 'Health diagnosing and treating practitioners and other technical occupations' for the civilian population age 16 and over",
    "text":"women working in health diagnosing and other medical occupations",
    "unit":"pop"
  },
  "employment_female_health_technologists_and_technicians":{  
    "api":"acs",
    "variable":"C24010_054E",
    "description":"Number of employed female 'Health technologists and technicians' for the civilian population age 16 and over",
    "text":"women working as health technicians",
    "unit":"pop"
  },
  "employment_female_service_occupations":{  
    "api":"acs",
    "variable":"C24010_055E",
    "description":"Number of employed female 'Service occupations:' for the civilian population age 16 and over",
    "text":"women who work in the service industry",
    "unit":"pop"
  },
  "employment_female_healthcare_support_occupations":{  
    "api":"acs",
    "variable":"C24010_056E",
    "description":"Number of employed female 'Healthcare support occupations' for the civilian population age 16 and over",
    "text":"women who work in healthcare support",
    "unit":"pop"
  },
  "employment_female_protective_service_occupations":{  
    "api":"acs",
    "variable":"C24010_057E",
    "description":"Number of employed female 'Protective service occupations:' for the civilian population age 16 and over",
    "text":"women who work in protective services",
    "unit":"pop"
  },
  "employment_female_fire_fighting_and_prevention_and_other_protective_service_workers_including_supervisors":{  
    "api":"acs",
    "variable":"C24010_058E",
    "description":"Number of employed female 'Fire fighting and prevention, or other protective service workers including supervisors' for the civilian population age 16 and over",
    "text":"women working in protective services",
    "unit":"pop"
  },
  "employment_female_law_enforcement_workers_including_supervisors":{  
    "api":"acs",
    "variable":"C24010_059E",
    "description":"Number of employed female 'Law enforcement workers including supervisors' for the civilian population age 16 and over",
    "text":"women law enforcement workers",
    "unit":"pop"
  },
  "employment_female_food_preparation_and_serving_related_occupations":{  
    "api":"acs",
    "variable":"C24010_060E",
    "description":"Number of employed female 'Food preparation and serving related occupations' for the civilian population age 16 and over",
    "text":"women who work in food prep",
    "unit":"pop"
  },
  "employment_female_building_and_grounds_cleaning_and_maintenance_occupations":{  
    "api":"acs",
    "variable":"C24010_061E",
    "description":"Number of employed female 'Building and grounds cleaning and maintenance occupations' for the civilian population age 16 and over",
    "text":"women who are groundskeepers and building maintenance workers",
    "unit":"pop"
  },
  "employment_female_personal_care_and_service_occupations":{  
    "api":"acs",
    "variable":"C24010_062E",
    "description":"Number of employed female 'Personal care and service occupations' for the civilian population age 16 and over",
    "text":"women working in personal care",
    "unit":"pop"
  },
  "employment_female_sales_and_office_occupations":{  
    "api":"acs",
    "variable":"C24010_063E",
    "description":"Number of employed female 'Sales and office occupations:' for the civilian population age 16 and over",
    "text":"women doing sales and office work",
    "unit":"pop"
  },
  "employment_female_sales_and_related_occupations":{  
    "api":"acs",
    "variable":"C24010_064E",
    "description":"Number of employed female 'Sales and related occupations' for the civilian population age 16 and over",
    "text":"women working in sales",
    "unit":"pop"
  },
  "employment_female_office_and_administrative_support_occupations":{  
    "api":"acs",
    "variable":"C24010_065E",
    "description":"Number of employed female 'Office and administrative support occupations' for the civilian population age 16 and over",
    "text":"women doing office admin work",
    "unit":"pop"
  },
  "employment_female_natural_resources_construction_and_maintenance_occupations":{  
    "api":"acs",
    "variable":"C24010_066E",
    "description":"Number of employed female 'Natural resources, construction, or maintenance occupations:' for the civilian population age 16 and over",
    "text":"women working in natural resources, construction, or maintenance",
    "unit":"pop"
  },
  "employment_female_farming_fishing_and_forestry_occupations":{  
    "api":"acs",
    "variable":"C24010_067E",
    "description":"Number of employed female 'Farming, fishing, or forestry occupations' for the civilian population age 16 and over",
    "text":"women farmers, fishers, or foresters",
    "unit":"pop"
  },
  "employment_female_construction_and_extraction_occupations":{  
    "api":"acs",
    "variable":"C24010_068E",
    "description":"Number of employed female 'Construction and extraction occupations' for the civilian population age 16 and over",
    "text":"women construction workers",
    "unit":"pop"
  },
  "employment_female_installation_maintenance_and_repair_occupations":{  
    "api":"acs",
    "variable":"C24010_069E",
    "description":"Number of employed female 'Installation, maintenance, or repair occupations' for the civilian population age 16 and over",
    "text":"women who work in repair and maintenance",
    "unit":"pop"
  },
  "employment_female_production_transportation_and_material_moving_occupations":{  
    "api":"acs",
    "variable":"C24010_070E",
    "description":"Number of employed female 'Production, transportation, or material moving occupations:' for the civilian population age 16 and over",
    "text":"women who work in factories, transit, or transportation of material goods",
    "unit":"pop"
  },
  "employment_female_production_occupations":{  
    "api":"acs",
    "variable":"C24010_071E",
    "description":"Number of employed female 'Production occupations' for the civilian population age 16 and over",
    "text":"women factory workers",
    "unit":"pop"
  },
  "employment_female_transportation_occupations":{  
    "api":"acs",
    "variable":"C24010_072E",
    "description":"Number of employed female 'Transportation occupations' for the civilian population age 16 and over",
    "text":"women transit workers",
    "unit":"pop"
  },
  "employment_female_material_moving_occupations":{  
    "api":"acs",
    "variable":"C24010_073E",
    "description":"Number of employed female 'Material moving occupations' for the civilian population age 16 and over",
    "text":"women who work in the transportation of material goods",
    "unit":"pop"
  },
  ## Poverty variables 
    "poverty":{  
    "api":"acs",
    "variable":"B17001_002E",
    "description":"Number of persons whose income in the past 12 months is below the poverty level",
    "text":"people living in poverty",
    "unit":"pop"
  },
  "poverty_male":{  
    "api":"acs",
    "variable":"B17001_003E",
    "description":"Number of male persons whose income in the past 12 months is below the poverty level",
    "text":"men living in poverty",
    "unit":"pop"
  },
  "poverty_female":{  
    "api":"acs",
    "variable":"B17001_017E",
    "description":"Number of female persons whose income in the past 12 months is below the poverty level",
    "text":"women living in poverty",
    "unit":"pop"
  },
  ## Demographic poverty 
    "poverty_white_alone":{  
    "api":"acs",
    "variable":"B17001A_002E",
    "description":"Number of persons whose income in the past 12 months is below the poverty level (White Alone)",
    "text":"white people living in poverty",
    "unit":"pop"
  },
  "poverty_black_alone":{  
    "api":"acs",
    "variable":"B17001B_002E",
    "description":"Number of persons whose income in the past 12 months is below the poverty level (Black or African American Alone)",
    "text":"Black people living in poverty",
    "unit":"pop"
  },
  "population_american_indian_alone":{  
    "api":"acs",
    "variable":"B17001C_002E",
    "description":"Number of persons whose income in the past 12 months is below the poverty level  (American Indian or Alaskan Native Alone)",
    "text":"native or indigenous people living in poverty",
    "unit":"pop"
  },
  "poverty_asian_alone":{  
    "api":"acs",
    "variable":"B17001D_002E",
    "description":"Number of persons whose income in the past 12 months is below the poverty level  (Asian Alone)",
    "text":"Asian people living in poverty",
    "unit":"pop"
  },
  "poverty_native_hawaiian_alone":{  
    "api":"acs",
    "variable":"B17001E_002E",
    "description":"Number of persons whose income in the past 12 months is below the poverty level  (Native Hawaiian and Other Pacific Islander Alone)",
    "text":"Pacific Islanders living in poverty",
    "unit":"pop"
  },
  "poverty_two_or_more_races":{  
    "api":"acs",
    "variable":"B17001G_002E",
    "description":"Number of persons whose income in the past 12 months is below the poverty level  (Two or more races)",
    "text":"mixed race people living in poverty",
    "unit":"pop"
  },
  "poverty_hispanic_origin":{  
    "api":"acs",
    "variable":"B17001I_002E",
    "description":"Number of persons whose income in the past 12 months is below the poverty level  (Hispanic Origin)",
    "text":"Hispanic-designated people living in poverty",
    "unit":"pop"
  },
  ## Family poverty 
    "poverty_family":{  
    "api":"acs",
    "variable":"B17012_002E",
    "description":"Number of families below the poverty level in the past 12 months",
    "text":"families living in poverty",
    "unit":"pop"
  },
  "poverty_family_married":{  
    "api":"acs",
    "variable":"B17012_003E",
    "description":"Number of married couples whose income is below the poverty level in the past 12 months",
    "text":"married couples living in poverty",
    "unit":"pop"
  },
  "poverty_family_single_male":{  
    "api":"acs",
    "variable":"B17012_009E",
    "description":"Number of families with a male householder and no wife present whose income is below the poverty level in the past 12 months",
    "text":"families raised by single dads living in poverty",
    "unit":"pop"
  },
  "poverty_family_single_female":{  
    "api":"acs",
    "variable":"B17012_014E",
    "description":"Number of families with a female householder and no husband present whose income is below the poverty level in the past 12 months",
    "text":"families raised by single moms living in poverty",
    "unit":"pop"
  },
  ## Age variables 
    "age":{  
    "api":"acs",
    "variable":"B01002_001E",
    "description":"Median age",
    "text":"median age",
    "unit":"age"
  },
  "median_male_age":{  
    "api":"acs",
    "variable":"B01002_002E",
    "description":"Median age by sex (male)",
    "text":"median age of men",
    "unit":"age"
  },
  "median_female_age":{  
    "api":"acs",
    "variable":"B01002_003E",
    "description":"Median age by sex (female)",
    "text":"median age of women",
    "unit":"age"
  },
  ## Population Variables 
    "population":{  
    "api":"acs",
    "variable":"B01003_001E",
    "description":"Total population",
    "text":"people",
    "unit":"pop"
  },
  "population_white_alone":{  
    "api":"acs",
    "variable":"B02001_002E",
    "description":"Population (White Alone)",
    "normalize_by":"population",
    "type":"percent",
    "text":"white",
    "unit":"race"
  },
  "population_black_alone":{  
    "api":"acs",
    "variable":"B02001_003E",
    "description":"Population (Black or African American Alone)",
    "normalize_by":"population",
    "type":"percent",
    "text":"Black",
    "unit":"race"
  },
  "population_american_indian_alone":{  
    "api":"acs",
    "variable":"B02001_004E",
    "description":"Population (American Indian or Alaskan Native Alone)",
    "normalize_by":"population",
    "type":"percent",
    "text":"native or indigenous",
    "unit":"race"
  },
  "population_asian_alone":{  
    "api":"acs",
    "variable":"B02001_005E",
    "description":"Population (Asian Alone)",
    "normalize_by":"population",
    "type":"percent",
    "text":"Asian",
    "unit":"race"
  },
  "population_native_hawaiian_alone":{  
    "api":"acs",
    "variable":"B02001_006E",
    "description":"Population (Native Hawaiian and Other Pacific Islander Alone)",
    "normalize_by":"population",
    "type":"percent",
    "text":"Pacific Islander",
    "unit":"race"
  },
  "population_two_or_more_races":{  
    "api":"acs",
    "variable":"B02001_008E",
    "description":"Population (Two or more races)",
    "normalize_by":"population",
    "type":"percent",
    "text":"mixed race",
    "unit":"race"
  },
  "population_hispanic_origin":{  
    "api":"acs",
    "variable":"B03001_003E",
    "description":"Population (Hispanic Origin)",
    "normalize_by":"population",
    "type":"percent",
    "text":"Hispanic",
    "unit":"race"
  },
  ## Housing 
    "median_house_construction_year":{  
    "api":"acs",
    "variable":"B25035_001E",
    "description":"Median year housing units were built",
    "text":"average home was built",
    "unit":"year"
  },
  "median_contract_rent":{  
    "api":"acs",
    "variable":"B25058_001E",
    "description":"Median contract rent",
    "text":"average rent",
    "unit":"dollars"
  },
  "median_gross_rent":{  
    "api":"acs",
    "variable":"B25064_001E",
    "description":"Median gross rent (contract rent plus the cost of utilities)",
    "text":"average cost of rent and utilities combined",
    "unit":"dollars"
  },
  "median_home_value":{  
    "api":"acs",
    "variable":"B25077_001E",
    "description":"Median value (dollars) for Owner-Occupied housing units",
    "text":"average value of an owner-occupied home",
    "unit":"dollars"
  },
  "median_monthly_owner_costs":{  
    "api":"acs",
    "variable":"B25088_002E",
    "description":"Median Selected Monthly Owner Costs (Dollars) by Mortgage Status",
    "text":"average monthly housing expense for a homeowner with a mortgage",
    "unit":"dollars"
  },
  ## Commute times 
    "commute_time_solo_automobile":{  
    "api":"acs",
    "variable":"B08136_003E",
    "description":"Time spent commuting (in minutes): Car, truck, or van - alone",
    "normalizable":True,
    "normalize_by":"transit_solo_automobile",
    "text":"commuting by car",
    "unit":"minutes"
  },
  "commute_time_carpool":{  
    "api":"acs",
    "variable":"B08136_004E",
    "description":"Time spent commuting (in minutes): Car, truck, or van - carpool",
    "normalizable":True,
    "normalize_by":"transit_carpool",
    "text":"commuting by carpool",
    "unit":"minutes"
  },
  "commute_time_public_transport":{  
    "api":"acs",
    "variable":"B08136_007E",
    "description":"Time spent commuting (in minutes): public transport (excluding taxis)",
    "normalizable":True,
    "normalize_by":"transit_public_transport",
    "text":"commuting by public transit",
    "unit":"minutes"
  },
  "commute_time_walked":{  
    "api":"acs",
    "variable":"B08136_011E",
    "description":"Time spent commuting (in minutes): walking",
    "normalizable":True,
    "normalize_by":"transit_walked",
    "text":"commuting by walking",
    "unit":"minutes"
  },
  "commute_time_other":{  
    "api":"acs",
    "variable":"B08136_012E",
    "description":"Time spent commuting (in minutes): Taxicab, motorcycle, bicycle, or other means",
    "normalizable":True,
    "normalize_by":"transit_other",
    "text":"commuting by taxi, motorcycle, bicycle, or other means",
    "unit":"minutes"
  },
  ## Transit means,raw numbers 
    "transit_total":{  
    "api":"acs",
    "variable":"B08301_001E",
    "description":"Means of Transportation to Work (total)",
    "normalizable":True,
    "text":"commute to work",
    "unit":"pop"
  },
  "transit_solo_automobile":{  
    "api":"acs",
    "variable":"B08301_003E",
    "description":"Means of Transportation to Work (Car, truck, or van - solo)",
    "normalizable":True,
    "normalize_by":"transit_total",
    "type":"percent",
    "text":"commute alone to work by car, truck, or van",
    "unit":"pop"
  },
  "transit_carpool":{  
    "api":"acs",
    "variable":"B08301_004E",
    "description":"Means of Transportation to Work (Car, truck, or van - carpool)",
    "normalizable":True,
    "normalize_by":"transit_total",
    "type":"percent",
    "text":"carpool to work by car, truck, or van",
    "unit":"pop"
  },
  "transit_public_transport":{  
    "api":"acs",
    "variable":"B08301_010E",
    "description":"Means of Transportation to Work (Public transportation (excluding taxicab))",
    "normalizable":True,
    "normalize_by":"transit_total",
    "type":"percent",
    "text":"commute to work by public transit",
    "unit":"pop"
  },
  "transit_walked":{  
    "api":"acs",
    "variable":"B08301_019E",
    "description":"Means of Transportation to Work (Walked)",
    "normalizable":True,
    "normalize_by":"transit_total",
    "type":"percent",
    "text":"commute to work by walking",
    "unit":"pop"
  },
  "transit_other":{  
    "api":"acs",
    "variable":"B08101_041E",
    "description":"Means of Transportation to Work (Taxicab, motorcycle, bicycle, or other means)",
    "normalizable":True,
    "normalize_by":"transit_total",
    "type":"percent",
    "text":"commute to work by taxi, motorcycle, bicycle, or other means",
    "unit":"pop"
  },
  ## Education 
    "education_none":{  
    "api":"acs",
    "variable":"B15003_002E",
    "description":"The number of persons age 25 and over who completed no schooling",
    "text":"people over 25 with no schooling at all",
    "unit":"pop"
  },
  "education_high_school":{  
    "api":"acs",
    "variable":"B15003_017E",
    "description":"The number of persons age 25 and over who have a regular high school diploma",
    "text":"people with a high school diploma",
    "unit":"pop"
  },
  "education_ged":{  
    "api":"acs",
    "variable":"B15003_018E",
    "description":"The number of persons age 25 and over who have a GED or alternative credential",
    "text":"people with a GED",
    "unit":"pop"
  },
  "education_associates":{  
    "api":"acs",
    "variable":"B15003_021E",
    "description":"The number of persons age 25 and over who hold an Associate's degree",
    "text":"people with an Associate's degree",
    "unit":"pop"
  },
  "education_bachelors":{  
    "api":"acs",
    "variable":"B15003_022E",
    "description":"The number of persons age 25 and over who hold a Bachelor's degree",
    "text":"people with a Bachelor's degree",
    "unit":"pop"
  },
  "education_masters":{  
    "api":"acs",
    "variable":"B15003_023E",
    "description":"The number of persons age 25 and over who hold a Master's degree",
    "text":"people with a Master's degree",
    "unit":"pop"
  },
  "education_professional":{  
    "api":"acs",
    "variable":"B15003_024E",
    "description":"The number of persons age 25 and over who hold a Professional degree",
    "text":"people with a Professional degree",
    "unit":"pop"
  },
  "education_doctorate":{  
    "api":"acs",
    "variable":"B15003_025E",
    "description":"The number of persons age 25 and over who hold a Doctoral degree",
    "text":"people with a Ph.D.",
    "unit":"pop"
  },
  ## language variables 
      "language_speak_only_english":{  
    "api":"acs",
    "variable":"B16001_002E",
    "description":"Speak_only_English",
    "text":"speak only English",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_spanish_or_spanish_creole":{  
    "api":"acs",
    "variable":"B16001_003E",
    "description":"Spanish_or_Spanish_Creole",
    "text":"speak Spanish or Spanish Creole",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_french_(incl._patois,_cajun)":{  
    "api":"acs",
    "variable":"B16001_006E",
    "description":"French_(incl._Patois,_Cajun)",
    "text":"speak French (incl. Patois, Cajun)",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_french_creole":{  
    "api":"acs",
    "variable":"B16001_009E",
    "description":"French_Creole",
    "text":"speak French Creole",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_italian":{  
    "api":"acs",
    "variable":"B16001_012E",
    "description":"Italian",
    "text":"speak Italian",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_portuguese_or_portuguese_creole":{  
    "api":"acs",
    "variable":"B16001_015E",
    "description":"Portuguese_or_Portuguese_Creole",
    "text":"speak Portuguese or Portuguese Creole",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_german":{  
    "api":"acs",
    "variable":"B16001_018E",
    "description":"German",
    "text":"speak German",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_yiddish":{  
    "api":"acs",
    "variable":"B16001_021E",
    "description":"Yiddish",
    "text":"speak Yiddish",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_greek":{  
    "api":"acs",
    "variable":"B16001_030E",
    "description":"Greek",
    "text":"speak Greek",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_russian":{  
    "api":"acs",
    "variable":"B16001_033E",
    "description":"Russian",
    "text":"speak Russian",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_polish":{  
    "api":"acs",
    "variable":"B16001_036E",
    "description":"Polish",
    "text":"speak Polish",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_serbo-croatian":{  
    "api":"acs",
    "variable":"B16001_039E",
    "description":"Serbo-Croatian",
    "text":"speak Serbo-Croatian",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_armenian":{  
    "api":"acs",
    "variable":"B16001_045E",
    "description":"Armenian",
    "text":"speak Armenian",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_persian":{  
    "api":"acs",
    "variable":"B16001_048E",
    "description":"Persian",
    "text":"speak Persian",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_gujarati":{  
    "api":"acs",
    "variable":"B16001_051E",
    "description":"Gujarati",
    "text":"speak Gujarati",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_hindi":{  
    "api":"acs",
    "variable":"B16001_054E",
    "description":"Hindi",
    "text":"speak Hindi",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_urdu":{  
    "api":"acs",
    "variable":"B16001_057E",
    "description":"Urdu",
    "text":"speak Urdu",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_chinese":{  
    "api":"acs",
    "variable":"B16001_066E",
    "description":"Chinese",
    "text":"speak Chinese",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_japanese":{  
    "api":"acs",
    "variable":"B16001_069E",
    "description":"Japanese",
    "text":"speak Japanese",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_korean":{  
    "api":"acs",
    "variable":"B16001_072E",
    "description":"Korean",
    "text":"speak Korean",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_mon-khmer,_cambodian":{  
    "api":"acs",
    "variable":"B16001_075E",
    "description":"Mon-Khmer,_Cambodian",
    "text":"speak Mon-Khmer",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_hmong":{  
    "api":"acs",
    "variable":"B16001_078E",
    "description":"Hmong",
    "text":"speak Hmong",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_thai":{  
    "api":"acs",
    "variable":"B16001_081E",
    "description":"Thai",
    "text":"speak Thai",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_laotian":{  
    "api":"acs",
    "variable":"B16001_084E",
    "description":"Laotian",
    "text":"speak Laotian",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_vietnamese":{  
    "api":"acs",
    "variable":"B16001_087E",
    "description":"Vietnamese",
    "text":"speak Vietnamese",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_tagalog":{  
    "api":"acs",
    "variable":"B16001_093E",
    "description":"Tagalog",
    "text":"speak Tagalog",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_navajo":{  
    "api":"acs",
    "variable":"B16001_099E",
    "description":"Navajo",
    "text":"speak Navajo",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_hungarian":{  
    "api":"acs",
    "variable":"B16001_105E",
    "description":"Hungarian",
    "text":"speak Hungarian",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_arabic":{  
    "api":"acs",
    "variable":"B16001_108E",
    "description":"Arabic",
    "text":"speak Arabic",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  },
  "language_hebrew":{  
    "api":"acs",
    "variable":"B16001_111E",
    "description":"Hebrew",
    "text":"speak Hebrew",
    "normalize_by":"population",
    "unit":"pop",
    "type":"percent"
  }
}