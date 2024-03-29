USE [master]
GO
/****** Object:  Database [Bibliotech]    Script Date: 11/1/2024 12:54:39 a. m. ******/
CREATE DATABASE [Bibliotech]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Bibliotech', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Bibliotech.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Bibliotech_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Bibliotech_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [Bibliotech] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Bibliotech].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Bibliotech] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Bibliotech] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Bibliotech] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Bibliotech] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Bibliotech] SET ARITHABORT OFF 
GO
ALTER DATABASE [Bibliotech] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Bibliotech] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Bibliotech] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Bibliotech] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Bibliotech] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Bibliotech] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Bibliotech] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Bibliotech] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Bibliotech] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Bibliotech] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Bibliotech] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Bibliotech] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Bibliotech] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Bibliotech] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Bibliotech] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Bibliotech] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Bibliotech] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Bibliotech] SET RECOVERY FULL 
GO
ALTER DATABASE [Bibliotech] SET  MULTI_USER 
GO
ALTER DATABASE [Bibliotech] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Bibliotech] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Bibliotech] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Bibliotech] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Bibliotech] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Bibliotech] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'Bibliotech', N'ON'
GO
ALTER DATABASE [Bibliotech] SET QUERY_STORE = ON
GO
ALTER DATABASE [Bibliotech] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [Bibliotech]
GO
/****** Object:  User [usuario2]    Script Date: 11/1/2024 12:54:39 a. m. ******/
-- CREATE USER [usuario2] WITHOUT LOGIN WITH DEFAULT_SCHEMA=[dbo]
-- GO
/****** Object:  Table [dbo].[Libros]    Script Date: 11/1/2024 12:54:39 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Libros](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[titulo] [varchar](200) NULL,
	[autor] [varchar](80) NULL,
	[editorial] [varchar](80) NULL,
	[año] [varchar](50) NOT NULL,
	[descripcion] [varchar](800) NULL,
	[imagen] [varchar](255) NULL,
	[url] [varchar](500) NULL,
	[categoria] [varchar](60) NULL,
	[id_user] [int] NULL,
 CONSTRAINT [PK_Libros] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[user]    Script Date: 11/1/2024 12:54:39 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[user](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[username] [varchar](15) NOT NULL,
	[email] [varchar](50) NOT NULL,
	[fullname] [varchar](50) NOT NULL,
	[password] [char](102) NOT NULL,
 CONSTRAINT [PK_user] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Libros] ON 

INSERT [dbo].[Libros] ([id], [titulo], [autor], [editorial], [año], [descripcion], [imagen], [url], [categoria], [id_user]) VALUES (107, N'Hábitos atómicos / Atomic Habits', N'James Clear', N'Editorial Planeta, S.A.U..', N'2020', N'A menudo pensamos que para cambiar de vida tenemos que pensar en hacer cambios grandes. Nada más lejos de la realidad. Según el reconocido experto en hábitos James Clear, el cambio real proviene del resultado de cientos de pequeñas decisiones: hacer dos flexiones al día, levantarse cinco minutos antes o hacer una corta llamada telefónica.

Clear llama a estas decisiones “hábitos atómicos”: tan pequeños como una partícula, pero tan poderosos como un tsunami. En este libro innovador nos revela exactamente cómo esos cambios minúsculos pueden crecer hasta llegar a cambiar nuestra carrera profesional, nuestras relaciones y todos los aspectos de nuestra vida.', N'2024000146_habitos.jpg', N'https://www.amazon.com/-/es/James-Clear/dp/6075694129?ref_=Oct_d_obs_d_16568978011_1&pd_rd_w=n3tXs&content-id=amzn1.sym.64a9023b-57cb-4cca-be91-e6361229d063&pf_rd_p=64a9023b-57cb-4cca-be91-e6361229d063&pf_rd_r=CCVPJ0TMVW4CNJPSC0WC&pd_rd_wg=KWkHj&pd_rd_r=fa7f77a8-2941-4be7-9286-614a30269dd7&pd_rd_i=6075694129', N'Autoayuda y Desarrollo Personal', 1)
INSERT [dbo].[Libros] ([id], [titulo], [autor], [editorial], [año], [descripcion], [imagen], [url], [categoria], [id_user]) VALUES (108, N'Padre Rico, Padre Pobre', N'Robert T. Kiyosaki', N'MENTES LIBRES', N'2022', N'El autor y conferencista Robert T. Kiyosaki desarrolló una perspectiva económica única a partir de la exposición que tuvo a dos influencias: su propio padre, altamente educado,  pero muy inestable y el padre multimillonario, sin educación universitaria, de su mejor amigo. Los problemas monetarios que su padre pobre experimentó toda la vida (con cheques mensuales muy respetables pero nunca suficientes) rompían con lo que le comunicaba su padre rico: que la clase pobre y la clase media trabajan por dinero, pero la clase alta hace que el dinero trabaje para ellos. Kiyosaki presenta la filosofía detrás de esta relación excepcional con el dinero.', N'2024002044_padre.jpg', N'https://www.amazon.com/-/es/Robert-T-Kiyosaki/dp/1644736624/ref=pd_bxgy_img_d_sccl_1/130-5082115-3768234?pd_rd_w=bZbsm&content-id=amzn1.sym.2b132e63-5dcd-4ba1-be9f-9e044543d59f&pf_rd_p=2b132e63-5dcd-4ba1-be9f-9e044543d59f&pf_rd_r=CT32H6BGJGA6224HZM9Q&pd_rd_wg=D7eiY&pd_rd_r=55a45949-7057-47f5-bf77-489ce2faa92b&pd_rd_i=1644736624&psc=1', N'Negocios y Finanzas', 1)
INSERT [dbo].[Libros] ([id], [titulo], [autor], [editorial], [año], [descripcion], [imagen], [url], [categoria], [id_user]) VALUES (109, N'El monje que vendió su Ferrari', N'Robin Sharma', N'', N'2019', N'El monje que vendió su Ferrari es una fábula espiritual que, desde hace más de quince años, ha marcado la vida de millones de personas en todo el mundo.
A través de sus páginas, conocemos la extraordinaria historia de Julian Mantle, un abogado de éxito que, tras sufrir un ataque al corazón, debe afrontar el gran vacío de su existencia. Inmerso en esta crisis existencial, Julian toma la radical decisión de vender todas sus pertenencias y viajar a la India. Es en un monasterio del Himalaya donde aprende las sabias y profundas lecciones de los monjes sobre la felicidad, el coraje, el equilibrio y la paz interior.', N'2024002340_MonjeQueVendioSuFerrari.jpg', N'https://www.amazon.com/-/es/Robin-Sharma/dp/1644730065/ref=bmx_dp_an35rb8n_d_sccl_2_9/130-5082115-3768234?pd_rd_w=uZ7uM&content-id=amzn1.sym.2d3e76dc-c4bd-4e07-8ec4-d52b40e7fd91&pf_rd_p=2d3e76dc-c4bd-4e07-8ec4-d52b40e7fd91&pf_rd_r=81MP8PJ8P6EFF7KR1E9H&pd_rd_wg=2VYjT&pd_rd_r=dead0272-5bca-4d10-a641-23480a839420&pd_rd_i=1644730065&psc=1', N'Negocios y Finanzas', 1)
INSERT [dbo].[Libros] ([id], [titulo], [autor], [editorial], [año], [descripcion], [imagen], [url], [categoria], [id_user]) VALUES (110, N'El sutil arte de que te importe un caraj*', N'Mark Manson', N'MENTES LIBRES', N'2020', N'Manson nos recuerda que los seres humanos somos falibles y limitados: ""no todos podemos ser extraordinarios: hay ganadores y perdedores en la sociedad, y esto no siempre es justo o es tu culpa"". Manson nos aconseja que reconozcamos nuestras limitaciones y las aceptemos. Esto es, según él, el verdadero origen del empoderamiento. Una vez que abrazamos nuestros temores, faltas e incertidumbres, una vez que dejamos de huir y evadir y empezamos a confrontar las verdades dolorosas, podemos comenzar a encontrar el valor, la perseverancia, la honestidad, la responsabilidad, la curiosidad y el perdón que buscamos.', N'2024002557_el sutil arte.jpg', N'https://www.amazon.com/-/es/Mark-Manson/dp/1400213304/ref=sr_1_1?crid=3EKE64N8KQ9JO&keywords=el+sutil+arte+de+que+te+importe+un+carajo&qid=1704947062&s=books&sprefix=sutil%2Cstripbooks-intl-ship%2C114&sr=1-1', N'Autoayuda y Desarrollo Personal', 1)
SET IDENTITY_INSERT [dbo].[Libros] OFF
GO
SET IDENTITY_INSERT [dbo].[user] ON 

INSERT [dbo].[user] ([id], [username], [email], [fullname], [password]) VALUES (1, N'Rusbel', N'rusbelrodriguez50@gmail.com', N'Rusbel Rodriguez', N'pbkdf2:sha256:600000$gmKWmZTiIf0D5nL0$d6edb864b2b3a2b821bc559cc248eeb024b4806531e81895d03f151850a3e687')
SET IDENTITY_INSERT [dbo].[user] OFF
GO
ALTER TABLE [dbo].[Libros]  WITH CHECK ADD  CONSTRAINT [FK_libros_usuario] FOREIGN KEY([id_user])
REFERENCES [dbo].[user] ([id])
GO
ALTER TABLE [dbo].[Libros] CHECK CONSTRAINT [FK_libros_usuario]
GO
USE [master]
GO
ALTER DATABASE [Bibliotech] SET  READ_WRITE 
GO
