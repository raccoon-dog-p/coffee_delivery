import styles from '../styles/NaviBar.module.css'
import { Link } from 'react-router-dom';
import logo from '../assets/logo.svg'
import cart from '../assets/cart.svg'

export default function NaviBar() {
    return (
        <header className={styles.header}>
            <nav className={styles.nav}>
            <Link to='/'>
                <img src={logo} style={styles.img}></img>
            </Link>
                <ul className={styles.ul}>
                    <Link to='/reservation' style={styles.a}>
                    <li className={styles.li}>예약 하기</li>
                    </Link>
                    <Link to='/beans' style={styles.a}>
                    <li className={styles.li}>원두 소개</li>
                    </Link>
                    <Link to='/menu' style={styles.a}>
                    <li className={styles.li}>메뉴 소개</li>
                    </Link>
                    <Link to='/notice' style={styles.a}>
                    <li className={styles.li}>공지 사항</li>
                    </Link>
                </ul>
                <ul className={styles.right_ul}>
                    <ul className={styles.ul}>
                        <li className={styles.li}>
                            <Link to='/signin'>
                            <button>로그인/회원가입</button>
                            </Link>
                        </li>
                        <div className={styles.div}>
                            <Link to='/cart'>
                            <img src={cart}></img>
                            </Link>
                        </div>
                    </ul>
                </ul>
            </nav>
        </header>
    );
}