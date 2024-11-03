
import Header from "@/Components/Header/Header"; 
import Topnav from "@/Components/Topnav/topnav"; 
import Image from "@/Components/Images/Image"; 

import styles from "./topnav.style.css";
import stylez from "./image.style.css";


export default function Page() {
  return (<>
    {/* <div className={styles.header}>
      <Header />
    </div> */}

    <div className={styles.header}>
      <Topnav />
    </div>

    <div className={stylez.image}>
      <Image/>
    </div>

    </>
  );
}
