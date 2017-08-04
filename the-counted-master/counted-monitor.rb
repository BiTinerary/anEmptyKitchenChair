#update skeleton.json from guardian's the counted project
# Skeletons file is just that.
#A list of people who are now dead as result of law enforcement.

require 'net/http'
require 'uri'

def fetch_url(url)
  url = URI.parse(url)
  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true if url.scheme == 'https'
  response = http.request_get(url.path)
  abort "HTTP error fetching '#{url.to_s}': '#{response.code}: #{response.message}'" unless response.kind_of?(Net::HTTPSuccess)
  return response.body
end

def fetchJsonLink()
	js_url = 'https://interactive.guim.co.uk/2015/the-counted/_list/boot.js'
	js = fetch_url(js_url)
	json_url_prefix = js.match(/https?:\/\/interactive\.guim\.co\.uk\/2015\/the-counted\/v\/\d+\//) or abort "Could not extract URL from #{js_url}"

	jsonLink = "#{json_url_prefix}files/skeleton.json"
	puts jsonLink
	return jsonLink
end

def fetchWAPOFile()
	gitUrl = 'https://github.com/washingtonpost/data-police-shootings'
	wAPOcsv = fetch_url(gitUrl)
	findCSV = wAPOcsv.match(/\/{1}.*\.csv" /) or abort "Could not extract URL from #{gitUrl}"
	print findCSV
end

def fetchFile(file)
	system("wget #{file}")
end

fetchFile(fetchJsonLink)