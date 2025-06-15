from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

def stop_warp():
    try:
        # Check WARP status
        status_result = subprocess.run(["warp-cli", "status"], capture_output=True, text=True)
        print("WARP Status:")
        print(status_result.stdout)
        # If WARP is connected, disconnect it
        if "Connected" in status_result.stdout:
            print("Stopping WARP...")
            disconnect_result = subprocess.run(["sudo", "warp-cli", "disconnect"], check=True)
            print("WARP stopped successfully.")
        else:
            print("WARP is not currently connected.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while stopping WARP: {e}")


def start_warp():
    try:
        # Check WARP status
        status_result = subprocess.run(["warp-cli", "status"], capture_output=True, text=True)
        print("WARP Status:")
        print(status_result.stdout)
        # Start WARP if not already connected
        if "Connected" not in status_result.stdout:
            print("Starting WARP...")
            subprocess.run(["sudo", "warp-cli", "--accept-tos", "connect"], check=True)
            print("WARP started successfully.")
        else:
            print("WARP is already connected.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while managing WARP: {e}")


def testtw():
    # Retrieve environment variables
    channel = "brutalles"
    authorization = "cnyavwlzoecwrspww62frgp6jqpxc7"
    client_id = "gp762nuuoqcoxypju8c569th9wz7q5"

    if not channel or not authorization or not client_id:
        print("Missing required environment variables: CHANNEL, AUTHORIZATION, or TCLIENTID.")
        return False

    # Set up the API request
    url = f"https://api.twitch.tv/helix/streams?user_login={channel}"
    headers = {
        "Authorization": f"Bearer {authorization}",
        "Client-Id": client_id
    }

    try:
        # Send the GET request to the Twitch API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Check if the response contains "live"
        if "live" in response.text:
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return False


def testkick():
    token_url = "https://id.kick.com/oauth/token"
    client_id = "01JRQWB2PV6KSB1RDJ790161BR"  # Replace with your client ID
    client_secret = "48fa80a0c3af9dda4985223e3aea16bd64d057538fbb62bf5836a1cb1e21c6b2"  # Replace with your client secret
    body = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    try:
        token_response = requests.post(token_url, data=body)
        token_response.raise_for_status()
        access_token = token_response.json().get("access_token")
        # print(f"Access Token: {access_token}")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving token: {client_id} {client_secret} {e}")
        return False

    channel_slug = "brutalles"  # Replace this with the channel's slug
    url = f"https://api.kick.com/public/v1/channels?slug={channel_slug}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json().get("data", [])
        for channel in data:
            slug = channel.get("slug")
            is_live = channel.get("stream", {}).get("is_live")
            if is_live is True:
                return True
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving channel data: {e}")
        return False

    return False

#resolution = get_random_resolution()
#start_warp()
with SB(uc=True, test=True) as sb:
    #sb.set_window_size(resolution.width, resolution.height)
    timp = random.randint(60,600)
    start_time = time.time()
    duration = timp * 60
    if time.time() - start_time < duration:
        if testkick():
            channel = "brutalles"
            url = f'https://kick.com/{channel}'
            sb.uc_open_with_reconnect(url, 5)
            sb.uc_gui_click_captcha()
            sb.sleep(1)
            sb.uc_gui_handle_captcha()
            sb.sleep(1)
            if sb.is_element_present('button:contains("Accept")'):
                sb.uc_click('button:contains("Accept")', reconnect_time=4)
            if sb.is_element_present('button:contains("I am 18+")'):
                sb.uc_click('button:contains("I am 18+")', reconnect_time=4)
            abosdia3 = sb.get_new_driver(undetectable=True)
            abosdia3.uc_open_with_reconnect(url, 5)
            abosdia3.uc_gui_click_captcha()
            sb.sleep(1)
            abosdia3.uc_gui_handle_captcha()
            sb.sleep(5)
            if abosdia3.is_element_present('button:contains("Accept")'):
                abosdia3.uc_click('button:contains("Accept")', reconnect_time=4)
            if abosdia3.is_element_present('button:contains("I am 18+")'):
                abosdia3.uc_click('button:contains("I am 18+")', reconnect_time=4)
            while testkick():
                if testkick():
                    sb.sleep(120)
                else:
                    break
            sb.quit_extra_driver()
        if testtw():
            channel = "brutalles"
            url = f'https://www.twitch.tv/{channel}'
            sb.uc_open_with_reconnect(url, 5)
            sb.uc_gui_click_captcha()
            sb.sleep(2)
            sb.uc_gui_handle_captcha()
            if sb.is_element_present('button:contains("Start Watching")'):
                sb.uc_click('button:contains("Start Watching")', reconnect_time=4)
            if sb.is_element_present('button:contains("Accept")'):
                sb.uc_click('button:contains("Accept")', reconnect_time=4)
            abosdia3 = sb.get_new_driver(undetectable=True)
            abosdia3.uc_open_with_reconnect(url, 5)
            abosdia3.uc_gui_click_captcha()
            sb.sleep(2)
            abosdia3.uc_gui_handle_captcha()
            sb.sleep(15)
            if abosdia3.is_element_present('button:contains("Start Watching")'):
                abosdia3.uc_click('button:contains("Start Watching")', reconnect_time=4)
            if abosdia3.is_element_present('button:contains("Accept")'):
                abosdia3.uc_click('button:contains("Accept")', reconnect_time=4)
            sb.sleep(5)
            while testtw():
                if testtw():
                    sb.sleep(12)
                else:
                    break
            sb.quit_extra_driver()

        sb.sleep(1)
