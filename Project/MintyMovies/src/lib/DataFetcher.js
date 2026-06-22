//Made by Lilly Andersen
//Modified by Jacob Ørnskov Andersen

import { browser } from '$app/env';
import { goto } from '$app/navigation';
// import { PUBLIC_API } from "$env/static/public";
const API_PATH = 'http://localhost:8010/';

export async function Get(endpoint, header = null) {
	let Header = {
		'Content-Type': 'application/json'
	};
	if (header != null) {
		for (let key in header) {
			Header[key] = header[key];
		}
	}

	return await fetch(API_PATH + endpoint, {
		method: 'GET',
		headers: Header
	})
		.then((response) => response.json())
		.then((data) => {
			return data;
		})
		.catch((reason) => {
			throw Error(reason);
		});
}

export async function Delete(endpoint, header = null) {
	let Header = {
		'Content-Type': 'application/json'
	};
	if (header != null) {
		for (let key in header) {
			Header[key] = header[key];
		}
	}

	return await fetch(API_PATH + endpoint, {
		method: 'DELETE',
		headers: Header
	})
		.then((response) => response.json())
		.then((data) => {
			return data;
		})
		.catch((reason) => {
			throw Error(reason);
		});
}

export async function Post(endpoint, body = null, header = null, form = false) {
	let Header = {};

	if (!form) {
		Header['Content-Type'] = 'application/json';
	}

	if (header != null) {
		for (let key in header) {
			Header[key] = header[key];
		}
	}

	let fetchBody = null;

	if (body != null) {
		if (form) {
			fetchBody = body;
		} else {
			fetchBody = {};
			for (let key in body) {
				fetchBody[key] = body[key];
			}
			fetchBody = JSON.stringify(fetchBody);
		}
	}

	return await fetch(API_PATH + endpoint, {
		method: 'POST',
		headers: Header,
		body: fetchBody
	})
		.then((response) => response.json())
		.then((data) => {
			return data;
		})
		.catch((reason) => {
			throw Error(reason);
		});
}

export async function Put(endpoint, body = null, header = null, form = false) {
	let Header = {};

	if (!form) {
		Header['Content-Type'] = 'application/json';
	}

	if (header != null) {
		for (let key in header) {
			Header[key] = header[key];
		}
	}

	let fetchBody = null;

	if (body != null) {
		if (form) {
			fetchBody = body;
		} else {
			fetchBody = {};
			for (let key in body) {
				fetchBody[key] = body[key];
			}
			fetchBody = JSON.stringify(fetchBody);
		}
	}

	return await fetch(API_PATH + endpoint, {
		method: 'PUT',
		headers: Header,
		body: fetchBody
	})
		.then((response) => response.json())
		.then((data) => {
			return data;
		})
		.catch((reason) => {
			throw Error(reason);
		});
}

export function GetSessionToken() {
    if (!browser) return null
	return localStorage.getItem('session_token');
}

export function SetSessionToken(token) {
	localStorage.setItem('session_token', token);
}

export function RemoveSessionToken() {
    localStorage.removeItem('session_token');
}