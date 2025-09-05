import Papa from 'papaparse';

export default async function importCsv(path: string) {
  const res = await fetch(path);
  const text = await res.text();
  return Papa.parse(text, {
    header: true,
    skipEmptyLines: true,
  }).data as Record<string, string>[];

}