require 'csv'

CSV.foreach('fatal-police-shootings-data.csv', :headers => true) do |row|
	firstName = row['name']
	bodyCam = row['body_camera']
	cod = row['manner_of_death']
	armed = row['armed']
	threat = row['threat_level']

	puts row[-1]
end

=begin
	if cod == "shot"
		if armed == 'unarmed'
			if threat == 'other'
				puts firstName
			end
		end
	end
=end