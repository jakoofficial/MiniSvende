import { GetSessionToken } from "$lib/DataFetcher";

export async function load() {
    const ses = GetSessionToken();
    return {
        ses: ses || null,
        loggedin: !!ses
    };
}