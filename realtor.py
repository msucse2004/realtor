from homeharvest import scrape_property
from datetime import datetime
import pandas as pd
OUTPUT_PATH = "output/"

class Hunting:
  def __init__(self, location, listing_type, past_days, property_type):
    self.location = location
    self.listing_type = listing_type
    self.past_days = 120  # sold in last 30 days - listed in last 30 days if (for_sale, for_rent)
    self.property_type = ['single_family', 'townhomes']


def main():
  # Generate filename based on current timestamp
  current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  filename = f"{OUTPUT_PATH}HomeHarvest_{current_timestamp}.csv"

  property_query = Hunting("Cary, NC", "for_sale", 120, ['single_family','townhomes'])

  properties = scrape_property(
    location=property_query.location,
    listing_type=property_query.listing_type,  # or (for_sale, for_rent, pending)
    past_days=property_query.past_days,  # sold in last 30 days - listed in last 30 days if (for_sale, for_rent)
    property_type=property_query.property_type,
    # date_from="2023-05-01", # alternative to past_days
    # date_to="2023-05-28",
    # foreclosure=True
    # mls_only=True,  # only fetch MLS listings
  )
  print(f"Number of properties: {len(properties)}")

  # Export to csv
  properties.to_csv(filename, index=False)
  print(properties.head())

if __name__ == "__main__":
    main()