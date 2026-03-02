curl 'https://api.flagsmith.com/api/v1/projects/34314/features/' \
  -H 'accept: */*' \
  -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
  -H 'authorization: Token 1344347780e05b6c742e214cdebe547dfa2f3335' \
  -H 'content-type: application/json' \
  -H 'origin: https://app.flagsmith.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://app.flagsmith.com/' \
  -H 'sec-ch-ua: "Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36' \
  --data-raw '{"initial_value":"Something","metadata":[],"name":"test_feature-1","tags":[],"project":34314,"type":"STANDARD"}'


  curl 'http://localhost:8000/api/v1/projects/1/features/?page=1&environment=2&page_size=50&is_archived=false&is_enabled=null&tag_strategy=INTERSECTION&value_search=&sort_field=name&sort_direction=ASC' \
  -H 'AUTHORIZATION: Token 27431915f15c02cb1eb0ea476663f404a43656ae' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
  -H 'Connection: keep-alive' \
  -b 'marketing_consent_given=true; t=27431915f15c02cb1eb0ea476663f404a43656ae' \
  -H 'Referer: http://localhost:8000/project/1/environment/YEQbH8vWbQyawCCLzBdDaQ/features?is_archived=false&page=1&sortBy=name&sortOrder=asc&tag_strategy=INTERSECTION' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"'
  