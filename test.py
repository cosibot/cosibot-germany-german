import requests


def get_stats(description, location):

    try:
        host = "api.data.decsis.cloud"
        query_fields = "[{\"cases_per_population\": \"field\"}, {\"death_rate\": \"field\"},{\"deaths\": \"field\"},{\"confirmed_accum\": \"field\"},{\"district\": \"field\"},{\"state\": \"field\"},{\"nuts\": \"field\"},{\"district_type\": \"field\"},{\"date_day\": \"field\"}]"

        # today = date.today()
        # query_filters = "[{\"date_day\":\"" + today.strftime("%Y-%m-%d")+"\"},{\""+ str(description) + "\":\""+ str(state_district) + "\"}]"
        query_filters = "[{\"" + str(description) + "\":\"" + str(location) + "\"}]"

        request_url = "https://" + host + "/api/v1/dataset/de_rki_covid19_landkreis?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json&limit=200&last-data=date_day"

        response = requests.get(url=request_url)
        json_response = (response.json())

        if (len(json_response) > 1):
            stats = json_response[0]
            stats['code'] = response.status_code
            stats['has_data'] = True
            stats['confirmed_accum'] = str(sum(c["confirmed_accum"] for c in json_response))
            stats['date_day'] = json_response[0]["date_day"]
            stats['deaths'] = str(sum(c["deaths"] for c in json_response))
            stats['state'] = json_response[0]["state"]

            return stats
        elif (len(json_response) == 1):
            stats = json_response[0]
            stats['code'] = response.status_code
            stats['had_data'] = True
            return stats
        else:
            # date_search = datetime.today() - timedelta(days=1)
            query_filters = "[{\"" + str(description) + "\":\"" + str(location) + "\"}]"

            request_url = "https://" + host + "/api/v1/dataset/de_rki_covid19_landkreis?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json&limit=200&last-data=date_day"
            response = requests.get(url=request_url)

            if (len(json_response) > 1):
                stats = json_response[0]
                stats['code'] = response.status_code
                stats['has_data'] = True
                stats['confirmed_accum'] = str(sum(c["confirmed_accum"] for c in json_response))
                stats['date_day'] = json_response[0]["date_day"]
                stats['deaths'] = str(sum(c["deaths"] for c in json_response))
                stats['state'] = json_response[0]["state"]

                return stats
            elif (len(json_response) == 1):
                stats = json_response[0]
                stats['code'] = response.status_code
                stats['had_data'] = True
                return stats
    except Exception:
        return {}


if __name__ == "__main__":
    description = "district"
    location = "Frankfurt"

    print(get_stats(description, location))
