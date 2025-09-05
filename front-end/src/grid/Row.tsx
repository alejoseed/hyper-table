import { useEffect, useState } from "react";
import importCsv  from "../parse_data/csvImport";

export default function Row() {
  const [rows, setRows] = useState<any[]>([]);

  useEffect(() => {
    importCsv("/first_name.csv").then(setRows);
  }, []);

  return <pre>{JSON.stringify(rows, null, 2)}</pre>;
}
