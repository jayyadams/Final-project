from app import app

from models import db, Cart, Customer, Store, Item, Checkout

from random import choice as rc

from faker import Faker

if __name__ == '__main__':
 with app.app_context():

    Item.query.delete()
    Customer.query.delete()
    Store.query.delete()
    Cart.query.delete()
    Checkout.query.delete()

    db.session.commit()


    fake = Faker()

    def seed_items():
            items = [
            Item(
                name="Josh Allen",
                position="QB",
                team="Buffalo Bills",
                avg_points=23,
                pos_rank=1,
                price=100,
                img='https://upload.wikimedia.org/wikipedia/commons/9/95/Josh_Allen_SEPT2021_%28cropped2%29.jpg',
                store_id= 1,
            ),
            Item(
                name="Jalen Hurts",
                position="QB",
                team="Philadelphia Eagles",
                avg_points=22,
                pos_rank=2,
                price=90,
                img='https://images.daznservices.com/di/library/DAZN_News/66/1f/hurts-20220919-getty-ftr_umucl7377d0qzxhorx2hu8ya.jpg?t=74358438&w=800',
                store_id= 1,
            ),
            Item(
                name="Justin Herbert",
                position="QB",
                team="Los Angeles Chargers",
                avg_points=21,
                pos_rank=3,
                price=80,
                img='https://frontofficesports.com/wp-content/uploads/2023/07/USATSI_20586879-scaled.jpg?quality=100',
                store_id= 1,
            ),
            Item(
                name="Lamar Jackson",
                position="QB",
                team="Baltimore Ravens",
                avg_points=19,
                pos_rank=4,
                price=70,
                img='https://static.www.nfl.com/image/upload/t_editorial_landscape_mobile/f_auto/league/mxuz1rfoc60uox3a70um.jpg',
                store_id= 1,
            ),
            Item(
                name="Sam Howell",
                position="QB",
                team="Washington Commanders",
                avg_points=18,
                pos_rank=5,
                price=60,
                img='https://media.nbcwashington.com/2023/11/sam-howell-commanders.jpg?quality=85&strip=all&resize=1200%2C675',
                store_id= 1,
            ),
            Item(
                name="Dak Prescott",
                position="QB",
                team="Dallas Cowboys",
                avg_points=19,
                pos_rank=6,
                price=50,
                img='https://library.sportingnews.com/styles/twitter_card_120x120/s3/2021-10/dak-prescott-101120-getty-ftr_10b19iyr5wky51oae9sstv9xyz.jpg?itok=p9Yr0F4A',
                store_id= 1,
            ),
            Item(
                name="CJ Stroud",
                position="QB",
                team="Houston Texans",
                avg_points=19,
                pos_rank=7,
                price=40,
                img='https://static.www.nfl.com/image/upload/t_editorial_landscape_mobile/f_auto/league/x1pg6fbbbgsyl5kqadbi.jpg',
                store_id= 1,
            ),
            Item(
                name="Joshua Dobbs",
                position="QB",
                team="Minnesota Vikings",
                avg_points=17,
                pos_rank=8,
                price=30,
                img='https://www.betus.com.pa/wp-content/uploads/2023/11/what-a-debut-for-josh-dobbs-11-06-2023.webp',
                store_id= 1,
            ),
            Item(
                name="Brock Purdy",
                position="QB",
                team="San Fransisco 49ers",
                avg_points=19,
                pos_rank=9,
                price=20,
                img='https://a57.foxsports.com/static-media.fox.com/fmc/prod/sports/6a686dda-78b3-4026-a02d-5af9b87d0ea6/1100/618/zoxihuklx9cnmcxj.jpg?ve=1&tl=1',
                store_id= 1,
            ),
            Item(
                name="Patrick Mahomes",
                position="QB",
                team="Kansas City Chiefs",
                avg_points=19,
                pos_rank=10,
                price=10,
                img='https://assets-global.website-files.com/646f83ebeb2de03609e8a7c0/6536a8044a7afdcc3a71c701_patrick-mahomes-kansas-city-chiefs-nfl_1qje6xo335txc1inyiy0miosap.png',
                store_id= 1,
            ),
            Item(
                name="Tyreek Hill",
                position="WR",
                team="Miami Dolphins",
                avg_points=26,
                pos_rank=1,
                price=100,
                img='https://www.si.com/.image/t_share/MjAxNjA4MzMyNzI3ODIxNjk3/tyreekhill_101523.jpg',
                store_id= 1,
            ),
            Item(
                name="Keenan Allen",
                position="WR",
                team="Los Angeles Chargers",
                avg_points=23,
                pos_rank=2,
                price=90,
                img='https://cloudfront-us-east-1.images.arcpublishing.com/bostonglobe/UHALXNPFYAOCFFKCVGMXYBOMSE.jpg',
                store_id= 1,
            ),
            Item(
                name="CeeDee Lamb",
                position="WR",
                team="Dallas Cowboys",
                avg_points=22,
                pos_rank=3,
                price=80,
                img='https://insidethestar.com/wp-content/uploads/2022/12/jazzmonet_cowboys-news_the-evolution-of-ceedee-lamb-what-the-box-score-doesnt-show-you.jpg',
                store_id= 1,
            ),
            Item(
               name="Stefon Diggs",
                position="WR",
                team="Buffalo Bills",
                avg_points=19,
                pos_rank=4,
                price=70,
                img='https://s.yimg.com/ny/api/res/1.2/1Bq1tUEhR.egjH6cU24rOQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://media.zenfs.com/en/buffalo_bills_wire_usa_today_sports_articles_253/bb2e1775252f0a9dca1df4475b3abd6f',
                store_id= 1,
            ),
            Item(
               name="AJ Brown",
                position="WR",
                team="Philadelphia Eagles",
                avg_points=21,
                pos_rank=5,
                price=60,
                img='https://media.nbcsportsphiladelphia.com/2023/10/web-231030-aj-brown-1.jpg?quality=85&strip=all&fit=3408%2C1917',
                store_id= 1,
            ),
            Item(
                name="Amon-Ra St Brown",
                position="WR",
                team="Detroit Lions",
                avg_points=22,
                pos_rank=6,
                price=50,
                img='https://cdn.profootballrumors.com/files/2022/09/AmonRa-St-Brown.jpg',
                store_id= 1,
            ),
            Item(
               name="JaMarr Chase",
                position="WR",
                team="Cincinnati Bengals",
                avg_points=19,
                pos_rank=7,
                price=40,
                img='https://static.www.nfl.com/image/private/t_editorial_landscape_12_desktop/league/ecavlwhkfzgidsbtadge',
                store_id= 1,
            ),
            Item(
                name="DJ Moore",
                position="WR",
                team="Chicago Bears",
                avg_points=17,
                pos_rank=8,
                price=30,
                img='https://cdn.theathletic.com/app/uploads/2023/09/05140918/GettyImages-1640676712-e1693937383760.jpg',
                store_id= 1,
            ),
            Item(
                name="Puka Nucua",
                position="WR",
                team="Los Angeles Rams",
                avg_points=18,
                pos_rank=9,
                price=20,
                img='https://sportshub.cbsistatic.com/i/r/2023/11/20/107f5e63-1ce5-435e-8efc-6021b955e956/thumbnail/1200x675/d3c7fed51cf693c3564b8e589eb19db7/puka.jpg',
                store_id= 1,
            ),
            Item(
                name="Adam Thielen",
                position="WR",
                team="Carolina Panthers",
                avg_points=18,
                pos_rank=10,
                price=10,
                img='https://cdn.vox-cdn.com/thumbor/kn4yCnjbOFajbDl3HBh_2XxD_PU=/0x0:7338x5253/1200x800/filters:focal(3576x506:4750x1680)/cdn.vox-cdn.com/uploads/chorus_image/image/72631703/1639110488.0.jpg',
                store_id= 1,
            ),
            Item(
                name="Christian McCaffrey",
                position="RB",
                team="San Fransisco 49ers",
                avg_points=24,
                pos_rank=10,
                price=100,
                img='https://static.49erswebzone.com/v/iZVWM4/content/media/cache/article-770x433-118aa365e59c012f453a4456a257060c.jpg',
                store_id= 1,
            ),
            Item(
                name="Raheem Mostert",
                position="RB",
                team="Miami Dolphins",
                avg_points=18,
                pos_rank=2,
                price=90,
                img='https://library.sportingnews.com/styles/twitter_card_120x120/s3/2023-10/Raheem%20Mostert%20101923.jpg?itok=TOugITIR',
                store_id= 1,
            ),
            Item(
                name="Travis Etienne Jr.",
                position="RB",
                team="Jacksonville Jaguars",
                avg_points=18,
                pos_rank=3,
                price=80,
                img='https://cdn.fantasypros.com/wp-content/images/Travis_Etienne_full-2_1470_647/716x384.jpg',
                store_id= 1,
            ),
            Item(
                name="Brian Robinson Jr.",
                position="RB",
                team="Washington Commanders",
                avg_points=15,
                pos_rank=4,
                price=70,
                img='https://phantom-marca.unidadeditorial.es/1b78118da4443ff61021edd56a2bbd29/resize/828/f/jpg/assets/multimedia/imagenes/2022/11/10/16681063267836.jpg',
                store_id= 1,
            ),
            Item(
                name="Josh Jacobs",
                position="RB",
                team="Las Vegas Raiders",
                avg_points=14,
                pos_rank=5,
                price=60,
                img='https://www.si.com/.image/c_fit%2Cw_620/MjAwMjM5OTY5MzAwNjUzMTY0/josh-jacobs.jpg',
                store_id= 1,
            ),
            Item(
                name="Rachaad White",
                position="RB",
                team="Tampa Bay Buccaneers",
                avg_points=15,
                pos_rank=6,
                price=50,
                img='https://static.www.nfl.com/image/private/t_editorial_landscape_12_desktop/league/y60qaxfzbcbmf8d7ciin',
                store_id= 1,
            ),
            Item(
                name="D'Andre Swift",
                position="RB",
                team="Philadelphia Eagles",
                avg_points=15,
                pos_rank=7,
                price=40,
                img='https://images.foxtv.com/static.fox29.com/www.fox29.com/content/uploads/2023/09/1280/720/GettyImages-1682035130.jpg?ve=1&tl=1',
                store_id= 1,
            ),
            Item(
                name="Jahmyr Gibbs",
                position="RB",
                team="Detroit Lions",
                avg_points=18,
                pos_rank=8,
                price=30,
                img='https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/Jahmyr-Gibbs.jpg?ve=1&tl=1',
                store_id= 1,
            ),
            Item(
                name="Alvin Kamara",
                position="RB",
                team="New Orleans Saints",
                avg_points=21,
                pos_rank=9,
                price=20,
                img='https://gray-wafb-prod.cdn.arcpublishing.com/resizer/wAIpxOC4c5krMkuqKtZkCUp6G2s=/1200x800/smart/filters:quality(85)/cloudfront-us-east-1.images.arcpublishing.com/gray/7XA3S2LDSFF5XF3NM6NQVG4454.jpg',
                store_id= 1,
            ),
            Item(
                 name="Joe Mixon",
                 position="RB",
                 team="Cincinnati Bengals",
                 avg_points=14,
                 pos_rank=10,
                 price=10,
                 img='https://static.clubs.nfl.com/image/private/t_person_squared_mobile/f_auto/bengals/hjdpldsorvgvh8d2zlrn.jpg',
                 store_id=1
           )
]

            
            db.session.add_all(items)

            db.session.commit()

    def seed_customers():
            customer = Customer(
                name="Guest",
                user_name="Guest1",
                password="12345QWERT!@",
                email="example@example.com",
                age= 26,
                membership=False,
            )
            db.session.add(customer)

            db.session.commit()

    def seed_stores():
            store = Store(
                name="Jordan Adams",
                password="@EaglesWIN11",
                email="jcadamsboomer@gmail.com",
                location="16300 Southwest Fwy",
            )
            db.session.add(store)

            db.session.commit()

    def seed_carts():
            cart = Cart(
                customer_id = 1
            )
            db.session.add(cart)

            db.session.commit()

    if __name__ == '__main__':
        with app.app_context():
            seed_items()  
            seed_customers()  
            seed_stores()
            seed_carts()

        print('Seeds growing ... ')
        print('')
        print('Game Day!')