#!/usr/bin/env ruby
#
class DownloadVulnHubTorrents
  require 'csv'

  def initialize
    @base_url = 'https://download.vulnhub.com'
  end

  # get the checksum file which has checksums + urls. we can automate the check of the files and compare with the checksums to make sure everything downloaded matches
  def download_checksum
    checksum_url = "#{@base_url}/checksum.txt"
    `wget #{checksum_url}` # download the checksum file
  end

  def gather_urls(filename)
    urls = `awk ' { print $2 } ' #{filename} | sed 's/^\./''/g' | grep -E 'ova|torrent|zip|tar|txt|gz|gzip|iso|7z|exe|text|img|png|jpg|jpeg|md|LICENSE|README'`
    CSV.parse(urls).flatten
  end
end
